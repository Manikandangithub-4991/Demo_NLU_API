# coding=utf-8
"""
Author : TH316641
Created on : 4/4/2017 5:19 PM
"""
class ConfigManager(object):
    """
        Class to provide the configuration details
    """

    url = "http://10.235.112.35:5003/api/v2/nlu/predict"
    nlu_url = "http://10.235.112.35:4000/api/v1/nlu/predict"

    chatbot_url = "http://10.235.112.34:5003/HolmesIT/chatbot/v2/api"

    sop_predict_url = "http://10.235.112.36:8021/api/v1/sopsync/predict"
    classifier_url = "http://10.235.112.36:8024/api/v1/Classifier/verifyAugBot"
    cogminer_url = "http://10.235.112.36:8090/api/v2/CogMiner/predict"
    ticket_query_url = "http://10.235.112.34:4003/api/v1/snow/createTicket"
    knowledgebot_url = "http://10.235.112.37:5121/faq/api/v1/knowledge/predict"