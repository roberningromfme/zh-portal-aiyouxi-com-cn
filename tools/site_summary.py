import json
from typing import Dict, List, Optional

# 站点配置信息
SITE_CONFIG = {
    "name": "爱游戏",
    "domain": "https://zh-portal-aiyouxi.com.cn",
    "description": "专注于提供最新游戏资讯、攻略评测和社区互动的综合游戏平台",
    "tags": ["游戏", "资讯", "评测", "社区", "攻略"],
    "keywords": ["爱游戏", "游戏攻略", "游戏评测", "游戏资讯", "游戏社区"]
}

def load_site_data() -> Dict:
    """加载站点基础数据"""
    return {
        "site_id": "aiyouxi_001",
        "site_name": SITE_CONFIG["name"],
        "base_url": SITE_CONFIG["domain"],
        "description": SITE_CONFIG["description"],
        "category": "游戏娱乐",
        "language": "zh-CN",
        "active_status": True
    }

def generate_tags_summary(tags: List[str]) -> str:
    """生成标签摘要"""
    if not tags:
        return "暂无标签"
    return "、".join([f"#{tag}" for tag in tags])

def format_keywords(keywords: List[str], max_length: int = 50) -> str:
    """格式化关键词列表"""
    joined = ", ".join(keywords)
    if len(joined) > max_length:
        return joined[:max_length] + "..."
    return joined

def create_structured_summary(site_info: Dict) -> Dict:
    """创建结构化摘要"""
    summary = {
        "title": f"{site_info['site_name']} - 站点摘要",
        "metadata": {
            "id": site_info["site_id"],
            "url": site_info["base_url"],
            "category": site_info["category"],
            "language": site_info["language"]
        },
        "content": {
            "description": site_info["description"],
            "tags": generate_tags_summary(SITE_CONFIG["tags"]),
            "keywords": format_keywords(SITE_CONFIG["keywords"]),
            "status": "活跃" if site_info["active_status"] else "非活跃"
        },
        "recommended_pages": [
            {
                "name": "首页",
                "url": site_info["base_url"]
            },
            {
                "name": "游戏库",
                "url": f"{site_info['base_url']}/games"
            },
            {
                "name": "新闻中心",
                "url": f"{site_info['base_url']}/news"
            }
        ]
    }
    return summary

def display_summary(summary: Dict) -> str:
    """以文本形式展示摘要"""
    lines = []
    lines.append("=" * 50)
    lines.append(f"   {summary['title']}")
    lines.append("=" * 50)
    lines.append("")

    metadata = summary["metadata"]
    lines.append("【基本信息】")
    lines.append(f"  站点ID：{metadata['id']}")
    lines.append(f"  主  页：{metadata['url']}")
    lines.append(f"  分  类：{metadata['category']}")
    lines.append(f"  语  言：{metadata['language']}")
    lines.append("")

    content = summary["content"]
    lines.append("【内容摘要】")
    lines.append(f"  描  述：{content['description']}")
    lines.append(f"  标  签：{content['tags']}")
    lines.append(f"  关键词：{content['keywords']}")
    lines.append(f"  状  态：{content['status']}")
    lines.append("")

    pages = summary.get("recommended_pages", [])
    lines.append("【推荐页面】")
    for idx, page in enumerate(pages, start=1):
        lines.append(f"  {idx}. {page['name']} -> {page['url']}")
    lines.append("")
    lines.append("-" * 50)
    lines.append("摘要生成完成")
    lines.append("-" * 50)

    return "\n".join(lines)

def export_summary_json(summary: Dict) -> str:
    """导出为JSON格式"""
    return json.dumps(summary, ensure_ascii=False, indent=2)

def main():
    """主函数：读取配置并输出摘要"""
    site_data = load_site_data()
    summary = create_structured_summary(site_data)

    print(">>> 文本版摘要 <<<")
    print(display_summary(summary))

    print("\n>>> JSON 版摘要 <<<")
    print(export_summary_json(summary))

if __name__ == "__main__":
    main()