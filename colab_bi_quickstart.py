#!/usr/bin/env python3
"""
Colab quickstart file for BI panel auto-interpretation workflow.

Usage in Colab:
1) Upload this file.
2) Run:
   !python colab_bi_quickstart.py --mode all
3) Generated files:
   - /content/bi_sft.json
   - /content/bi_sft_text.jsonl
"""

from __future__ import annotations

import argparse
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List


def check_runtime() -> None:
    try:
        import torch  # type: ignore

        print("torch:", torch.__version__)
        print("cuda available:", torch.cuda.is_available())
        if torch.cuda.is_available():
            print("device:", torch.cuda.get_device_name(0))
    except Exception as exc:
        print("runtime check warning:", exc)


def build_bi_dataset(output_path: str = "/content/bi_sft.json", n_samples: int = 200) -> Path:
    random.seed(42)
    base_date = datetime(2026, 3, 7)

    rows: List[Dict[str, str]] = []
    for i in range(n_samples):
        day = (base_date - timedelta(days=i)).strftime("%Y-%m-%d")
        gmv = round(random.uniform(800, 3500), 2)
        conv = round(random.uniform(1.2, 4.5), 2)
        refund = round(random.uniform(1.0, 12.0), 2)
        roas = round(random.uniform(1.5, 6.5), 2)
        gmv_mom = round(random.uniform(-0.25, 0.25), 3)

        report = {
            "date": day,
            "metrics": {
                "gmv_wan": gmv,
                "conversion_pct": conv,
                "refund_pct": refund,
                "roas": roas,
                "gmv_mom": gmv_mom,
            },
        }

        summary = (
            f"{day}日报：GMV {gmv}万元，转化率 {conv}%，退款率 {refund}%，ROAS {roas}，"
            f"GMV环比 {gmv_mom * 100:.1f}%。"
        )
        advice = "建议优先排查异常指标对应渠道，并补充次日跟踪动作。"

        rows.append(
            {
                "instruction": "请解读这份BI日报并给出结论与建议",
                "input": json.dumps(report, ensure_ascii=False),
                "output": f"{summary} {advice}",
            }
        )

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print("saved dataset:", out, "samples:", len(rows))
    return out


def to_chat_text(sample: Dict[str, str]) -> str:
    return (
        "<|im_start|>system\n"
        "你是企业BI分析助手，输出要简洁、准确、可执行。\n"
        "<|im_end|>\n"
        "<|im_start|>user\n"
        f"{sample['instruction']}\n"
        f"{sample['input']}\n"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
        f"{sample['output']}\n"
        "<|im_end|>"
    )


def export_text_jsonl(
    dataset_path: str = "/content/bi_sft.json",
    output_jsonl: str = "/content/bi_sft_text.jsonl",
) -> Path:
    data = json.loads(Path(dataset_path).read_text(encoding="utf-8"))
    out = Path(output_jsonl)
    out.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8") as f:
        for row in data:
            f.write(json.dumps({"text": to_chat_text(row)}, ensure_ascii=False) + "\n")

    print("saved text jsonl:", out, "rows:", len(data))
    return out


def route_model(result_json: Dict[str, object]) -> str:
    required = ["summary", "risks", "actions", "confidence"]
    if any(k not in result_json for k in required):
        return "qwen3.5-2B"
    if float(result_json.get("confidence", 0)) < 0.75:
        return "qwen3.5-2B"
    return "qwen3.5-0.8B"


def run_demo_router() -> None:
    sample_a = {"summary": "ok", "risks": [], "actions": ["keep"], "confidence": 0.82}
    sample_b = {"summary": "low confidence", "risks": ["drop"], "actions": ["check channel"], "confidence": 0.43}
    print("router sample A ->", route_model(sample_a))
    print("router sample B ->", route_model(sample_b))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mode",
        choices=["runtime", "dataset", "text", "router", "all"],
        default="all",
        help="Which module to run.",
    )
    parser.add_argument("--samples", type=int, default=200, help="Dataset sample size.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.mode in ("runtime", "all"):
        check_runtime()
    if args.mode in ("dataset", "all"):
        build_bi_dataset(n_samples=args.samples)
    if args.mode in ("text", "all"):
        export_text_jsonl()
    if args.mode in ("router", "all"):
        run_demo_router()

    print("done.")


if __name__ == "__main__":
    main()
