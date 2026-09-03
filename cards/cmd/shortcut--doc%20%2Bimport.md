# dws doc +import

kind: shortcut
completeness: full
description: 上传本地文件并等待转换成在线文档对象；白名单外格式自动改走文件上传原样入库
source: internal/shortcut/doc/content_shortcuts.go:575
visible_flags: 4

## Flags
- --file <String>: 工作目录内已存在文件的相对路径
- --folder <String>: 可选目标文件夹 ID；与 workspace 互斥；在线转换格式省略二者时解析当前组织唯一 orgSpace 根目录
- --workspace <String>: 可选目标知识库 ID；与 folder 互斥；在线转换格式省略二者时解析当前组织唯一 orgSpace 根目录
- --name <String>: 导入后名称

## Related
- dws doc +background-delete
- dws doc +background-update
- dws doc +checkpoint-update
- dws doc +comment-create
- dws doc +comment-create-inline
- dws doc +comment-delete
