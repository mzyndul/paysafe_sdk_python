#!/usr/bin/env python3
'''
Created on 1-June-2016

@author: Asawari.Vaidya
'''
from PythonPaysafeSDK.CustomerVault.ACHBankAccount import ACHBankAccount
from PythonPaysafeSDK.DirectDebit.Purchase import Purchase
from PythonPaysafeSDK.PaysafeApiClient import PaysafeApiClient
from utils.Utils import Utils

from Config import Config
from RandomTokenGenerator import RandomTokenGenerator


optimal_obj = PaysafeApiClient(Config.api_key, Config.api_password, Config.environment, Config.account_number)
purchase_obj = Purchase(None)
purchase_obj.merchantRefNum(RandomTokenGenerator().generateToken())
purchase_obj.amount(100.98 * Config.currency_base_units_multiplier)

achbank_obj = ACHBankAccount(None)
achbank_obj.payMethod("WEB")
achbank_obj.paymentToken("DeZpXwrWtKIt8pN")
purchase_obj.ach(achbank_obj)

response_object = optimal_obj.direct_debit_service_handler().submit_purchase(purchase_obj)

print ("\nResponse Values ==========> ")
Utils.print_response(response_object)

