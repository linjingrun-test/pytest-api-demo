import requests
import pytest

# 模拟 环保资源回收交易系统 接口域名（模拟地址，无真实后端）
BASE_URL = "http://mock-test-demo.local"

class TestRecycleTradeApi:
    """
    模拟：环保资源回收交易系统接口测试
    测试模块：登录、资源发布、订单创建、权限校验
    """

    def test_user_login_success(self):
        """正常用户登录-正向场景"""
        url = f"{BASE_URL}/api/user/login"
        payload = {"username": "test01", "password": "123456"}
        resp = requests.post(url, json=payload)
        # 断言
        assert resp.status_code == 200
        assert resp.json().get("code") == 0

    def test_user_login_param_error(self):
        """登录-参数异常：密码为空，异常场景（等价类/边界用例）"""
        url = f"{BASE_URL}/api/user/login"
        payload = {"username": "test01", "password": ""}
        resp = requests.post(url, json=payload)
        assert resp.status_code in [200,400]
        assert resp.json().get("code") != 0

    def test_publish_resource(self):
        """发布回收资源-正常业务场景"""
        headers = {"token":"mock_token_123456"}
        url = f"{BASE_URL}/api/resource/publish"
        body = {
            "res_name":"废旧纸箱",
            "res_type":"纸类",
            "price":1.2
        }
        resp = requests.post(url,json=body,headers=headers)
        assert resp.json().get("code") == 0

    def test_publish_resource_no_token(self):
        """发布资源-无token权限校验，未登录禁止提交"""
        url = f"{BASE_URL}/api/resource/publish"
        body = {
            "res_name":"废旧纸箱",
            "res_type":"纸类",
            "price":1.2
        }
        resp = requests.post(url,json=body)
        # 未登录返回鉴权失败
        assert resp.json().get("code") == 401

    def test_create_trade_order(self):
        """创建回收交易订单"""
        headers = {"token":"mock_token_123456"}
        url = f"{BASE_URL}/api/order/create"
        body = {
            "resource_id":1001,
            "buyer_id":2001,
            "num":5
        }
        resp = requests.post(url,json=body,headers=headers)
        assert resp.json().get("code") ==0


if __name__ == "__main__":
    pytest.main(["-v"])
