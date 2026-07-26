"""
SafeOption AI v3.1.3 Freeze Candidate - Bilingual Text Support
===============================================
v3.1 BASELINE — preserved in full.
"""

TEXTS = {
    'English': {
        'app_title': 'SafeOption AI',
        'app_subtitle': 'Options Education & Risk Analysis Platform',
        'disclaimer': (
            'Educational simulation only. Not financial advice. '
            'This application does not execute trades.'
        ),
        'language_label': 'Language',
        'strategy_label': 'Strategy',
        'sell_put': 'Sell Put (Cash-Secured)',
        'buy_call': 'Buy Call',
        'mode_label': 'Mode',
        'live_chain': 'Market-Linked Educational Chain',
        'simulation': 'Simulation',
        'stock_symbol_section': 'Underlying Stock',
        'stock_symbol': 'Stock Symbol',
        'load_market_price': 'Load Current Price',
        'market_price_failed': 'Market price was not updated.',
        'market_data_scope': (
            'Current stock price only. Option strikes and analytics remain '
            'educational/model-generated.'
        ),
        'underlying_price': 'Underlying Price ($)',
        'dte_label': 'Days to Expiration',
        'dte_presets': 'Quick DTE Selection',
        'strike_label': 'Strike Price',
        'sim_strike_label': 'Enter Strike Price (Simulation)',
        'iv_label': 'Implied Volatility (%)',
        'risk_free_rate': 'Risk-Free Rate (%)',
        'contracts_label': 'Number of Contracts',
        'calculate': 'Analyze Position',
        'results_title': 'Position Analysis',
        'option_price': 'Option Price (per share)',
        'option_price_total': 'Total Premium',
        'max_profit': 'Max Profit',
        'max_loss': 'Max Loss',
        'breakeven': 'Breakeven',
        'risk_level': 'Risk Level',
        'prob_profit': 'Probability of Profit',
        'capital_required': 'Capital Required',
        'expiration_date': 'Expiration Date',
        'greeks_title': 'Option Greeks',
        'delta': 'Delta',
        'gamma': 'Gamma',
        'theta': 'Theta (per day)',
        'vega': 'Vega (per 1% IV)',
        'rho': 'Rho (per 1% rate)',
        'education_title': 'Educational Explanation',
        'strategy_explanation': 'Strategy Explanation',
        'risk_explanation': 'Risk Analysis',
        'terminology_title': 'Key Terminology',
        'dividend_risk': 'Dividend Risk',
        'earnings_risk': 'Earnings Risk',
        'assignment_risk': 'Assignment Risk',
        'no_results': 'No results. Please check your inputs.',
        'sell_put_education': (
            "A Cash-Secured Put involves selling a put option while holding "
            "enough cash to purchase the underlying stock at the strike price. "
            "The seller collects the premium upfront and profits if the stock "
            "price remains above the strike at expiration. Maximum profit is "
            "limited to the premium received; maximum loss occurs if the stock "
            "falls to zero (strike minus premium, times 100 shares per contract)."
        ),
        'buy_call_education': (
            "A Long Call involves buying a call option, granting the right "
            "(not obligation) to purchase the stock at the strike price. "
            "The buyer pays the premium and profits if the stock rises above "
            "strike plus premium. Maximum loss is limited to premium paid; "
            "maximum profit is theoretically unlimited."
        ),
        'risk_low': (
            'LOW — Conservative position with lower potential return. '
            'Suitable for income-focused strategies with defined risk.'
        ),
        'risk_medium': (
            'MEDIUM — Moderate risk with balanced risk/reward. '
            'Monitor position regularly.'
        ),
        'risk_high': (
            'HIGH — Elevated risk. Requires active monitoring and '
            'may require timely adjustments.'
        ),
        'risk_very_high': (
            'VERY HIGH — Significant risk. Recommended only for '
            'experienced traders with robust risk management.'
        ),
        'dividend_info': (
            'If the underlying pays a dividend before expiration, '
            'early assignment risk increases for in-the-money puts. '
            'Monitor ex-dividend dates relative to expiration.'
        ),
        'earnings_info': (
            'Earnings announcements can cause significant price movements. '
            'Consider the earnings date relative to option expiration.'
        ),
        'assignment_info': (
            'For short puts, if stock falls below strike at expiration, '
            'you may be assigned shares at the strike price. Ensure '
            'sufficient cash is available (cash-secured).'
        ),
        'market_params': 'Market Parameters',
        'days_unit': 'days',
        'configure_prompt': 'Configure parameters and click Analyze Position.',
        'qa_panel': 'QA Status',
        'qa_dte': 'DTE Linkage',
        'qa_sim': 'Simulation Mode',
        'qa_calc': 'Calculations',
        'qa_bilingual': 'Bilingual',
    },
    '中文': {
        'app_title': 'SafeOption AI',
        'app_subtitle': '期权教育与风险分析平台',
        'disclaimer': '仅供期权教育与模拟使用，不构成投资建议，本程序不执行任何交易。',
        'language_label': '语言',
        'strategy_label': '策略',
        'sell_put': '卖出看跌期权（现金担保）',
        'buy_call': '买入看涨期权',
        'mode_label': '模式',
        'live_chain': '市场价格联动教学链',
        'simulation': '模拟模式',
        'stock_symbol_section': '标的股票',
        'stock_symbol': '股票代码',
        'load_market_price': '读取当前股价',
        'market_price_failed': '股价未更新。',
        'market_data_scope': '这里只读取当前股价；期权行权价和分析仍由教学模型生成。',
        'underlying_price': '标的价格 ($)',
        'dte_label': '到期天数',
        'dte_presets': '快速DTE选择',
        'strike_label': '行权价',
        'sim_strike_label': '输入行权价（模拟）',
        'iv_label': '隐含波动率 (%)',
        'risk_free_rate': '无风险利率 (%)',
        'contracts_label': '合约数量',
        'calculate': '分析持仓',
        'results_title': '持仓分析',
        'option_price': '期权价格（每股）',
        'option_price_total': '总权利金',
        'max_profit': '最大利润',
        'max_loss': '最大亏损',
        'breakeven': '盈亏平衡价',
        'risk_level': '风险等级',
        'prob_profit': '盈利概率',
        'capital_required': '所需资金',
        'expiration_date': '到期日',
        'greeks_title': '期权希腊值',
        'delta': 'Delta',
        'gamma': 'Gamma',
        'theta': 'Theta（每日）',
        'vega': 'Vega（每1%波动率）',
        'rho': 'Rho（每1%利率）',
        'education_title': '教育说明',
        'strategy_explanation': '策略说明',
        'risk_explanation': '风险分析',
        'terminology_title': '关键术语',
        'dividend_risk': '股息风险',
        'earnings_risk': '财报风险',
        'assignment_risk': '行权指派风险',
        'no_results': '暂无结果。请检查输入参数。',
        'sell_put_education': (
            "现金担保看跌期权是指在持有足够现金以行权价买入标的股票的情况下，"
            "卖出看跌期权。卖方预先收取权利金，若到期时股价保持在行权价之上即可获利。"
            "最大利润限于收取的权利金，最大亏损发生在股价跌至零时"
            "（行权价减去权利金，乘以每张合约100股）。"
        ),
        'buy_call_education': (
            "买入看涨期权是指购买一份看涨期权合约，赋予持有者"
            "以行权价买入标的股票的权利（而非义务）。"
            "买方预先支付权利金，若股价上涨超过行权价加上已付权利金即可获利。"
            "最大亏损限于已付权利金，最大利润理论上无上限。"
        ),
        'risk_low': '低风险 — 保守型持仓，潜在收益较低。适合以收益为导向、风险可控的策略。',
        'risk_medium': '中等风险 — 风险/收益平衡适中。请定期监控持仓。',
        'risk_high': '高风险 — 风险提升。需要主动监控，可能需要及时调整或平仓。',
        'risk_very_high': '极高风险 — 风险显著。仅建议有经验的交易者使用，并需完善的风险管理。',
        'dividend_info': (
            '若标的股票在期权到期前派发股息，实值看跌期权的提前行权风险将增加。'
            '请关注除息日与到期日的关系。'
        ),
        'earnings_info': (
            '财报公告可能导致股价剧烈波动。'
            '评估风险时请考虑财报日期与期权到期日的关系。'
        ),
        'assignment_info': (
            '对于卖出看跌期权，若到期时股价跌破行权价，'
            '您可能被指派以行权价买入股票。请确保有充足资金（现金担保）。'
        ),
        'market_params': '市场参数',
        'days_unit': '天',
        'configure_prompt': '请配置参数后点击"分析持仓"。',
        'qa_panel': 'QA状态',
        'qa_dte': 'DTE联动',
        'qa_sim': '模拟模式',
        'qa_calc': '计算引擎',
        'qa_bilingual': '双语切换',
    },
}


def get_text(lang, key):
    return TEXTS.get(lang, TEXTS['English']).get(key, key)
