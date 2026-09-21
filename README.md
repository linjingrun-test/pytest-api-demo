# pytest‑api‑demo
> 演示基于 Python + pytest + requests 的接口自动化测试Demo
> 原型参考：环保资源回收交易系统（个人练习Demo，非公司内部源码）

## 📋项目说明
模拟环保资源回收交易Web系统部分接口自动化用例；
覆盖场景：
1. 登录正向、参数异常场景
2. 资源发布业务接口
3. Token权限控制鉴权测试
4. 交易订单创建接口
使用pytest做用例管理，requests发起http请求，添加业务断言。

## 环境依赖
