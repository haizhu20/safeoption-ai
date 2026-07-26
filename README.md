# SafeOption AI v3.1.3

**Frozen Educational Simulation Release / 冻结教学模拟版**

SafeOption AI is a bilingual options education and risk-analysis application.
It helps beginners explore how strategy, strike price, time to expiration,
volatility, interest rate, and contract quantity affect an illustrative
options position.

SafeOption AI 是一个双语期权教育与风险分析程序，帮助初学者观察策略、
行权价、到期时间、隐含波动率、无风险利率和合约数量如何影响示范性期权持仓。

> **Educational simulation only. Not financial advice.
> This application does not execute trades.**
>
> **本程序仅供期权教育与模拟使用，不构成投资建议，也不执行任何交易。**

---

## Our Purpose / 项目初心

**Orion Team Project Slogan / Orion团队项目口号**

> **“Education First. Risk First.”**
> **“教育第一，风险第一。”**

Options education should begin with **survival and risk**, not with the promise
of profit. Before asking how much a trade might earn, a beginner should first
understand what can be lost, where the risk comes from, and whether that risk
can be managed and endured.

SafeOption AI was created by the Orion team to lower the learning barriers
surrounding options and to make risk awareness more accessible to ordinary
people. We believe AI should help people understand financial risk—not simply
trade faster. Through clear explanations, interactive simulation, and
multilingual support, we aim to help learners from different language and
technical backgrounds develop informed, responsible, and independent
judgment.

SafeOption AI provides the educational concepts and risk-analysis framework.
The related **Orion Options Case Library（期权交易百战实例库）** records
real-world decisions, outcomes, uncertainties, mistakes, and lessons. Together,
they connect knowledge with practice: one explains the principles, while the
other tests and enriches them through real cases.

**Safety Over Hype. Learn the risk before taking the trade.**

期权教育的起点应当是**生存与风险**，而不是对盈利的承诺。在询问一笔交易
可能赚多少钱以前，初学者首先应当理解：可能损失什么、风险来自哪里，以及
自己能否管理和承受这种风险。

Orion团队创建SafeOption AI，是为了降低期权学习门槛，让普通人也能获得清楚、
易懂的风险教育。我们认为，AI应当帮助人们理解金融风险，而不只是让交易变得
更快。通过清晰解释、互动模拟和多语言支持，我们希望帮助不同语言、不同技术
背景的学习者形成知情、负责和独立的判断能力。

SafeOption AI提供知识框架和风险分析工具；与它相关的
**Orion期权交易百战实例库**记录真实交易中的决策、结果、不确定性、错误和
经验。两者把知识与实践连接起来：前者解释原理，后者通过真实案例检验并丰富
这些原理。

**安全重于炒作。交易之前，先学会理解风险。**

---

## English

### Release status

Version **3.1.3** is the frozen Phase 1 baseline release. It passed:

- 48 automated tests with 0 failures;
- independent QA review by Oreo M;
- final interactive product acceptance by Hai;
- state-consistency regression checks for stock-symbol and strike changes.

Future development involving real option chains, broker APIs, real-time
Greeks, or trade execution belongs in a separate **v4.x** development line.
No new features should be added to v3.1.3.

### Intended audience and distribution

This repository is the **open-source developer edition**. It is intended for
developers, researchers, educators, and technically experienced users who can
install Python dependencies and run a Streamlit application.

It is not yet the final consumer installation package. The next stage is to
explore more accessible editions for non-technical users, including a
one-click Windows edition, a hosted web edition that can be opened directly in
a browser, and a possible future mobile edition. The Windows edition is
intended to provide a standard launcher or installer without requiring users
to install Python, open PowerShell, or enter command-line instructions. These
consumer editions are planned future work and are not included in v3.1.3.

### Main features

- English and Chinese interface;
- Sell Put (Cash-Secured) and Buy Call education;
- Market-Linked Educational Chain and Simulation modes;
- stock-symbol input and latest available stock-price lookup;
- quick DTE selection: 7, 14, 30, 45, and 60 days;
- manual strike-price entry in Simulation mode;
- illustrative premium, breakeven, maximum profit/loss, capital requirement,
  probability, risk level, and Greeks;
- automatic invalidation of old results when calculation inputs change;
- visible protection against invalid or unavailable stock symbols.

### Market-data boundary

The application retrieves only the latest available **underlying stock
price** through `yfinance`.

Option strikes, premiums, implied volatility, Greeks, probabilities, and risk
analysis are user-supplied or model-generated for educational purposes. The
“Market-Linked Educational Chain” is **not** a live broker option chain.

Market data may be delayed, incomplete, or unavailable. Always verify values
independently before using them for learning or discussion.

### Installation and launch

Python 3.10 or later is recommended.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app\streamlit_app.py
```

macOS or Linux:

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app/streamlit_app.py
```

Streamlit normally opens the application automatically. Otherwise, use the
local URL shown in the terminal, commonly `http://localhost:8501`.

### Tests

```bash
python -m pytest -q
```

Expected frozen-baseline result:

```text
48 passed
```

### Acceptance evidence

Final manual acceptance screenshots are stored under `docs/screenshots/`:

- bilingual homepage and disclaimer;
- market-price lookup;
- Sell Put result;
- Buy Call result;
- 7-day and 60-day DTE behavior;
- invalid-symbol protection;
- result invalidation after changing the strike price.

---

## 中文

### 发布状态

**v3.1.3** 是 SafeOption AI 第一阶段正式冻结的基线版本，已经通过：

- 48项自动测试，0项失败；
- Oreo M 独立QA审查；
- Hai 最终交互式产品验收；
- 股票代码和行权价变化后的状态一致性回归测试。

以后涉及真实期权链、券商API、实时希腊值或交易执行的开发，统一进入独立的
**v4.x** 开发线。v3.1.3 不再增加新功能。

### 适用对象与发行方式

本仓库是面向开发者的**开源版本**，主要供开发者、研究人员、教育工作者及
具备一定技术经验、能够安装Python依赖并运行Streamlit程序的用户使用。

它还不是面向普通用户的最终安装包。下一阶段计划探索更方便的普通用户版本，
包括一键式Windows版、可通过浏览器直接访问的托管网络版，以及未来可能开发的
手机版。Windows版将采用标准启动程序或安装程序，使非技术用户不需要安装
Python、打开PowerShell或输入命令行指令即可使用。这些普通用户版本属于后续
开发计划，不包含在v3.1.3之中。

### 主要功能

- 中文和英文界面；
- 卖出看跌期权（现金担保）与买入看涨期权教学；
- “市场价格联动教学链”和“模拟模式”；
- 股票代码输入及最新可用股票价格读取；
- 7、14、30、45和60天快速到期日选择；
- 模拟模式下手动输入任意合理行权价；
- 示范性权利金、盈亏平衡价、最大利润/亏损、所需资金、盈利概率、
  风险等级和希腊值；
- 计算参数改变后自动清除过期分析结果；
- 无效或无法读取的股票代码具有清楚的错误保护。

### 市场数据边界

本程序通过 `yfinance` 读取的真实市场数据，仅限最新可用的
**标的股票价格**。

期权行权价、权利金、隐含波动率、希腊值、概率和风险分析，均由用户输入或
教学模型生成。“市场价格联动教学链”**不是真实券商期权链**。

市场数据可能延迟、不完整或暂时无法获得。用于学习和讨论前，应通过其他
可靠来源独立核对。

### 安装与启动

建议使用 Python 3.10 或更高版本。

```bash
python -m venv .venv
```

Windows PowerShell：

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m streamlit run app\streamlit_app.py
```

macOS 或 Linux：

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m streamlit run app/streamlit_app.py
```

Streamlit 通常会自动打开程序。若没有自动打开，请使用终端显示的本地网址，
一般为 `http://localhost:8501`。

### 运行测试

```bash
python -m pytest -q
```

冻结基线的预期结果：

```text
48 passed
```

### 验收证据

最终人工验收截图存放在 `docs/screenshots/`，包括：

- 双语首页与免责声明；
- 市场价格读取；
- Sell Put 分析结果；
- Buy Call 分析结果；
- 7天与60天DTE联动；
- 无效股票代码保护；
- 修改行权价后旧分析结果自动清除。

---

## Version history / 版本历史

| Version / 版本 | Role / 定位 |
|---|---|
| v3.1 | Approved baseline architecture / 批准的基础架构 |
| v3.1.2 | DTE, strike input, and workflow improvements / DTE、行权价输入及流程改进 |
| **v3.1.3** | Frozen Phase 1 educational baseline / 第一阶段正式冻结教学基线 |

## License / 许可证

See `LICENSE` in the repository. / 请参阅仓库中的 `LICENSE` 文件。
