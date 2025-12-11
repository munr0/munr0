import yaml

with open("langs.yaml") as f:
    config = yaml.safe_load(f)

lines = []
for category in config["categories"]:
    lines.append(f"### {category['stars']}&nbsp;&nbsp;{category['name']}")
    badges = []
    for lang_id in category["languages"]:
        lang = config["languages"][lang_id]
        logo_color = lang.get("logo_color", config["badge_config"]["logo_color"])
        url = f"{config['badge_config']['base_url']}/{lang['name']}-{lang['color']}?style={config['badge_config']['style']}&logoColor={logo_color}&logo={lang['logo']}"
        badges.append(
            f'<img alt="{lang["name"]}" src="{url}">{config["badge_config"]["spacing"]}'
        )
    lines.append("\n".join(badges))
    lines.append("")

with open("out.md", "w") as f:
    f.write("\n".join(lines))

print("Successfully generated out.md")
