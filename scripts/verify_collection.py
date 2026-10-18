#!/usr/bin/env python3
"""Check the curated collection manifest against its delivered files."""
import json
from pathlib import Path, PurePosixPath
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]


class UniqueLoader(yaml.SafeLoader):
    pass


def mapping(loader, node):
    values = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node)
        if key in values:
            raise ValueError(f"duplicate YAML key: {key}")
        values[key] = loader.construct_object(value_node)
    return values


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def main():
    manifest = json.loads((ROOT / "collection.json").read_text(), object_pairs_hook=_unique_json)
    if (set(manifest) != {"schema", "name", "skills", "commands", "materialized"}
            or type(manifest["schema"]) is not int or manifest["schema"] != 1
            or manifest["name"] != "pennix-skills-extra"):
        raise ValueError("invalid collection manifest header")
    entries = manifest["skills"]
    names = set(entries)
    dirs = {path.name for path in (ROOT / "skills").glob("*/*") if path.is_dir()}
    if names != dirs:
        raise ValueError("manifest members differ from delivered Skill directories")
    for name, entry in entries.items():
        if set(entry) != {"path", "license"}:
            raise ValueError(f"invalid entry: {name}")
        path = PurePosixPath(entry["path"])
        if path.is_absolute() or ".." in path.parts or path.name != name:
            raise ValueError(f"unsafe entry path: {name}")
        skill = ROOT.joinpath(*path.parts, "SKILL.md")
        text = skill.read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        metadata = yaml.load(match[1], Loader=UniqueLoader) if match else None
        if not isinstance(metadata, dict) or metadata.get("name") != name:
            raise ValueError(f"Skill identity mismatch: {name}")
        if entry["license"] and not (skill.parent / entry["license"]).is_file():
            raise ValueError(f"license missing: {name}")
    if manifest["commands"] or manifest["materialized"]:
        raise ValueError("extra collection does not publish commands or materialized Skills")
    print(f"verified {len(names)} curated Skills")


def _unique_json(pairs):
    value = {}
    for key, item in pairs:
        if key in value:
            raise ValueError(f"duplicate JSON key: {key}")
        value[key] = item
    return value


if __name__ == "__main__":
    main()
