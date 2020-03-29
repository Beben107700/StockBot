#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author : Romain Graux
@date : Saturday, 28 March 2020
"""

from .reward_strategy_base import Reward_Strategy
from .simple_reward_strategy import Simple_Reward_Strategy
from stockBot.finance import Wallet

class Aggressive_Reward_Strategy(Simple_Reward_Strategy):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def _get_reward(self, wallet:Wallet) -> float:
        # raise NotImplementedError("get_reward not implemented")
        self._push_balance_history(wallet.balance)

        returns = self._balance_history.pct_change().dropna() + 1
        arr = np.cumprod(returns.values) - 1

        reward = arr[-1] if len(arr) > 0 else 0

        reward = -10*reward if reward<0 else reward

        return reward
