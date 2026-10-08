---
source_path: "skills/mono/references/products/oa/template/components/SignatureField.md"
source_commit: "251ae0d7"
layer: mirror   # 逐字镜像,正文与上游一致,勿手工修改
---

# 手写签名 — `SignatureField`

> 分类：增强控件

手写签名采集。

## JSON Schema

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `componentName` | string | 是 | 固定值 `"SignatureField"` |
| `props.id` | string | 是 | 唯一标识，格式 `SignatureField_{随机字符串}` |
| `props.label` | string | 是 | 控件标题 |
| `props.required` | boolean | 否 | 是否必填，默认 false |
| `props.readFromLast` | boolean | 否 | 是否读取上次签名，默认 true |

## 示例

```json
{
  "componentName": "SignatureField",
  "props": {
    "id": "SignatureField_2044ROW9EFZ40",
    "label": "手写签名",
    "required": false,
    "readFromLast": true
  }
}
```
