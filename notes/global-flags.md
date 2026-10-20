---
title: 根命令参数与叶子参数的证据范围
maintenance: manual
intents: global_flags
triggers: 全局参数, 继承参数, --profile, --client-id, --client-secret, --debug, --dry-run, --fields, --format, -f, --jq, --mock, --timeout, --verbose, -v, --yes, -y, --output, -o, --token
contract:
  - 叶子命令卡的 visible_flags 只说明该卡列出的局部定义；判断参数是否支持必须同时核对根命令注册与对应命令的局部定义、示例和使用代码，不能据叶子表缺项直接否定。
---

# 根命令参数与叶子参数的证据范围

- 根命令通过 bindPersistentFlags 注册持久参数。这里的参数需要纳入子命令的语法核验；语法接受不等于命令会按猜测的业务语义使用它。
  {{code: internal/app/root.go | bindPersistentFlags(root, flags)}}
  {{code: internal/app/flags.go | GlobalFlags contains the root-level persistent flags shared across the CLI.}}
- 根级短别名也属于参数证据：`--format/-f`、`--verbose/-v`、`--yes/-y`、`--output/-o`；`output` 被隐藏不代表不存在。遇到同名局部参数仍先核对当前命令，不能把根级业务语义覆盖到局部定义。
  {{code: internal/app/flags.go | cmd.PersistentFlags().StringVarP(&flags.Format, "format", "f"}}
  {{code: internal/app/flags.go | cmd.PersistentFlags().BoolVarP(&flags.Verbose, "verbose", "v"}}
  {{code: internal/app/flags.go | cmd.PersistentFlags().BoolVarP(&flags.Yes, "yes", "y"}}
  {{code: internal/app/flags.go | cmd.PersistentFlags().StringVarP(&flags.Output, "output", "o"}}
  {{code: internal/app/flags.go | cmd.PersistentFlags().MarkHidden("output")}}
- `--profile` 在根命令注册，说明为“一次性指定组织或账号”；支持 corpId/corpName 与 userId/userName 组合，推荐 corpId:userId，多个按 CSV 逗号分隔。
  {{code: internal/app/flags.go | cmd.PersistentFlags().StringVar(&flags.Profile, "profile"}}
- `auth login` 的源码示例明确包含 `dws auth login --profile <corpId>`，说明为指定本次授权目标组织、不持久切换当前组织。因此不能因为 login 叶子卡未列出 profile 就说它不接受该参数；更细的身份选择仍需核对登录代码，不应仅由占位符推断。
  {{code: internal/app/auth_command.go | dws auth login --profile <corpId>}}
