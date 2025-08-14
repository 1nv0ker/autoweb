
        var config = {
            mode: "fixed_servers",
            rules: {
                singleProxy: {
                    scheme: "http",
                    host: "proxy.bitip.com",
                    port: parseInt(10001)
                },
                bypassList: ["localhost", "127.0.0.1"]
            }
        };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "1b7g3stpcswvnbitip_g-DE_f-129029g9h9g1",
                    password: "127939ghg92g2f28"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
            callbackFn,
            {urls: ["<all_urls>"]},
            ['blocking']
        );
        