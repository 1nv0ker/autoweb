def inject_request_interceptor(tab):
    """注入JS代码，拦截XHR和fetch请求"""
    # 注入的JavaScript代码：重写XMLHttpRequest和fetch，收集请求信息
    js_code = """
    // 存储请求信息的数组（全局变量，供Python读取）
    window.capturedRequests = [];

    // 拦截XMLHttpRequest
    (function() {
        const originalXhrOpen = XMLHttpRequest.prototype.open;
        const originalXhrSend = XMLHttpRequest.prototype.send;

        XMLHttpRequest.prototype.open = function(method, url) {
            this._requestInfo = {
                type: 'XHR',
                method: method,
                url: url,
                headers: {},
                body: null
            };
            return originalXhrOpen.apply(this, arguments);
        };

        // 拦截setRequestHeader，收集请求头
        XMLHttpRequest.prototype.setRequestHeader = function(header, value) {
            if (this._requestInfo) {
                this._requestInfo.headers[header] = value;
            }
            return XMLHttpRequest.prototype.setRequestHeader.apply(this, arguments);
        };

        // 拦截send，收集请求体
        XMLHttpRequest.prototype.send = function(body) {
            if (this._requestInfo) {
                this._requestInfo.body = body;
                // 存储请求信息
                window.capturedRequests.push(this._requestInfo);
            }
            return originalXhrSend.apply(this, arguments);
        };
    })();

    // 拦截fetch请求
    (function() {
        const originalFetch = window.fetch;
        window.fetch = async function(url, options = {}) {
            // 收集fetch请求信息
            const requestInfo = {
                type: 'fetch',
                method: options.method || 'GET',
                url: url.toString(),
                headers: options.headers ? Object.fromEntries(options.headers.entries()) : {},
                body: options.body ? await options.body.text() : null
            };
            console.log('requestInfo', requestInfo)
            // 存储请求信息
            window.capturedRequests.push(requestInfo);
            // 执行原始fetch
            return originalFetch.apply(this, arguments);
        };
    })();
    """
    # 注入JS代码到页面
    tab.run_js(js_code)

def get_captured_requests(tab):
    """从浏览器全局变量中获取捕获的请求信息"""
    # 读取window.capturedRequests并清空（避免重复获取）
    requests = tab.run_js("""
        
        return 123
    """)
    return requests