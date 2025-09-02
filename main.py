import http.server
import socket
import random
import sys

# サーバーの設定
HOST = '0.0.0.0'
PORT = 80

# リクエストを処理するハンドラクラス
class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    """ GETリクエストを処理するクラス """
    
    def do_GET(self):
        """ GETリクエストを受け取った際の処理 """
        
        # 1から10までの乱数を生成し、1が出たらサーバーを終了
        if random.randint(1, 10) == 1:
            print("🤖 1/10の確率が引かれました。サーバーをシャットダウンします...")
            # クライアントに応答を返さずにプロセスを終了
            sys.exit()

        # 9/10の確率で成功した場合の処理
        try:
            # ステータスコード 200 (成功) を送信
            self.send_response(200)
            # ヘッダーを送信
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()

            # ホスト名を取得してレスポンスとして書き込む
            hostname = socket.gethostname()
            message = f"<h1>✅ サーバーは正常です</h1><p>ホスト名: {hostname}</p>"
            self.wfile.write(message.encode('utf-8'))

        except Exception as e:
            print(f"エラーが発生しました: {e}")

def run_server(server_class=http.server.HTTPServer, handler_class=MyRequestHandler, host=HOST, port=PORT):
    """ サーバーを起動する関数 """
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    
    print(f"サーバーを http://{host}:{port} で起動します。")
    print("ブラウザでアクセスして動作を確認してください。")
    print("ページをリロードするたびに1/10の確率でサーバーが停止します。")
    print("サーバーを手動で停止するには Ctrl+C を押してください。")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nサーバーを手動で停止しました。")
    except SystemExit:
        print("サーバーが確率により停止しました。")
    finally:
        httpd.server_close()

if __name__ == '__main__':
    run_server()
