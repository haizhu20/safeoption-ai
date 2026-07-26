# Changelog / 版本记录

## v3.1.3 — Phase 1 Frozen Educational Baseline

### Added / 新增

- Restored bilingual stock-symbol input and latest available stock-price lookup.
- Added final acceptance screenshots and bilingual QA summary.
- Added bilingual project purpose, developer-edition positioning, and future
  consumer-distribution direction to the README.
- 恢复双语股票代码输入和最新可用股票价格读取。
- 加入最终验收截图及双语QA摘要。
- README加入项目初心、开发者版本定位和未来普通用户发行方向。

### Improved / 改进

- Quick DTE linkage for 7, 14, 30, 45, and 60 days.
- Arbitrary manual strike input in Simulation mode.
- Clearer “Market-Linked Educational Chain” terminology.
- 7、14、30、45和60天DTE联动。
- 模拟模式支持任意合理行权价手动输入。
- 明确采用“市场价格联动教学链”术语。

### Fixed / 修复

- Old results are invalidated when calculation inputs change.
- Changing or failing to load a stock symbol no longer leaves analysis from the
  previous stock visible.
- 计算参数变化后自动清除旧结果。
- 股票代码改变或读取失败后，不再保留上一股票的分析结果。

### Product boundary / 产品边界

Only the latest available underlying stock price is market-linked. Option
parameters and analysis remain user-supplied or model-generated for education.
The application does not execute trades or provide financial advice.

只有最新可用标的股票价格与市场联动；期权参数和分析仍由用户输入或教学模型
生成。本程序不执行交易，也不构成投资建议。
