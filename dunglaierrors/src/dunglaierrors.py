import colorama,time,sys,os,random
from io import StringIO
import contextlib
import threading

def init():
    colorama.init(autoreset=True)
class Loading:
    def __init__(self):
        self._running = True
    def terminate(self):
        self._running = False
        print(colorama.Fore.RESET, end="")
    def run(self, text):
        alltypes = ['|','/','-','\\','|','/','-','\\']
        while self._running:
            for i in range(len(alltypes)):
                sys.stdout.write("\r" + colorama.Fore.LIGHTCYAN_EX + text + ' ' + "đang hoạt động..." + alltypes[i])
                sys.stdout.flush()
                time.sleep(0.3)
    

class Docs:
    def doitiente(self) -> str:
        '''
        Thông tin về cách chuyển đổi tiền tệ (Vd: USD -> VND)
        '''
        _1 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Cách chuyển đổi tiền tệ (Vd: USD -> VND)' + ' ' + '-'*20 + colorama.Fore.RESET
        _2 = colorama.Fore.LIGHTCYAN_EX + '1. Xác định tỉ giá USD/VND, 1 USD = 23.000 VND' + colorama.Fore.RESET
        _3 = colorama.Fore.LIGHTCYAN_EX + '2. Tính tổng tiền cần chuyển đổi' + colorama.Fore.RESET
        _4 = colorama.Fore.LIGHTCYAN_EX + '3. Tính tổng tiền sau khi chuyển đổi' + colorama.Fore.RESET
        _5 = colorama.Fore.LIGHTCYAN_EX + '4. Hiển thị kết quả' + colorama.Fore.RESET
        _7 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example code' + ' ' + '-'*20 + colorama.Fore.RESET
        _8 = colorama.Fore.LIGHTCYAN_EX + '''
USD = int(input('Nhập số tiền USD: '))
VND = USD * 23000
print('Số tiền sau khi chuyển đổi là: ', VND)
        ''' + colorama.Fore.RESET
        _9 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example Input' + ' ' + '-'*20 + colorama.Fore.RESET
        _10 = colorama.Fore.LIGHTCYAN_EX + '''
Nhập số tiền USD: 100
        ''' + colorama.Fore.RESET
        _11 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example Output' + ' ' + '-'*20 + colorama.Fore.RESET
        _12 = colorama.Fore.LIGHTCYAN_EX + '''
Số tiền sau khi chuyển đổi là: 2300000
        ''' + colorama.Fore.RESET
        _13 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'End of text' + ' ' + '-'*20 + colorama.Fore.RESET
        return '\n'.join([_1,_2,_3,_4,_5,_7,_8,_9,_10,_11,_12,_13])
    
    def ifelse(self) -> str:
        '''
        Thông tin về cách sử dụng if else
        Tạo đấm lá kéo
        '''
        _1 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Cách sử dụng if else' + ' ' + '-'*20 + colorama.Fore.RESET
        _2 = colorama.Fore.LIGHTCYAN_EX + '1. Kiểm tra giá trị của biến' + colorama.Fore.RESET
        _3 = colorama.Fore.LIGHTCYAN_EX + '2. Nếu giá trị biến là True thì thực hiện các lệnh' + colorama.Fore.RESET
        _4 = colorama.Fore.LIGHTCYAN_EX + '3. Nếu giá trị biến là False thì thực hiện các lệnh' + colorama.Fore.RESET
        _5 = colorama.Fore.LIGHTCYAN_EX + '4. Hiển thị kết quả' + colorama.Fore.RESET
        _7 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example code' + ' ' + '-'*20 + colorama.Fore.RESET
        # making rock, paper, scissors game with if else
        _8 = colorama.Fore.LIGHTCYAN_EX + '''
import random

player = input('Nhập chọn của bạn: ')
computer = random.choice(['Kéo', 'Búa', 'Bao'])

if player == 'Kéo':
    if computer == 'Kéo':
        print('Hòa')
    elif computer == 'Búa':
        print('Thắng')
    else:
        print('Thua')

elif player == 'Búa':
    if computer == 'Kéo':
        print('Thua')
    elif computer == 'Búa':
        print('Hòa')
    else:
        print('Thắng')

elif player == 'Bao':
    if computer == 'Kéo':
        print('Thắng')
    elif computer == 'Búa':
        print('Thua')
    else:
        print('Hòa')

else:
    print('Nhập sai chọn')
        ''' + colorama.Fore.RESET
        _9 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example Input' + ' ' + '-'*20 + colorama.Fore.RESET
        _10 = colorama.Fore.LIGHTCYAN_EX + '''
Nhập chọn của bạn: Kéo
        ''' + colorama.Fore.RESET
        _11 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example Output' + ' ' + '-'*20 + colorama.Fore.RESET
        _12 = colorama.Fore.LIGHTCYAN_EX + '''
Hòa
        ''' + colorama.Fore.RESET
        _13 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'End of text' + ' ' + '-'*20 + colorama.Fore.RESET
        return '\n'.join([_1,_2,_3,_4,_5,_7,_8,_9,_10,_11,_12,_13])

    def fakeAI(self):
        '''
        Lo mà học Machine Learning với toán đi, ở đó mà AI if else
        '''
        return colorama.Fore.RED + "Học toán với ML đi bro, AI if else xong đi khoe hả :) ?" + colorama.Fore.RESET

    def keylogger(self):
        return colorama.Fore.YELLOW + "https://github.com/MHP0920/keylogger-advanced" + colorama.Fore.RESET 
class Check:
    def __init__(self):
        self.wordlist = []
        self.total_dumb = 0
        self.total_smart = 0
        self.random_num = str(random.randint(1, 100))
    @contextlib.contextmanager
    def stdoutIO(self, stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old
    def analyze_basic(self, text:str):
        text = text.lower().strip()
        if any(x in text for x in ['xin lỗi', 'know', 'sorry']):
            
            self.total_dumb += 1
        elif any (x in text for x in ['tôi', 'you']):
            return
        elif text:
            self.total_smart += 1
    def custom_input(self):
        return self.random_num
    def no_exit(self):
        return None
    def done(self):
        if self.wordlist:
            choz = random.choice(self.wordlist)
            self.wordlist.remove(choz)
            return choz
        else:
            return 'tạm biệt'
    def usdtovnd(self, code_or_path) -> str:
        '''
        Kiểm tra code chuyển đổi USD sang VND của bạn có đúng không
        '''
        _1 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'USD to VND Checker' + ' ' + '-'*20 + colorama.Fore.RESET
        _2 = ''
        _3 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Module' + ' ' + '-'*20 + colorama.Fore.RESET
        _4 = colorama.Fore.LIGHTCYAN_EX + '> Đã load!' + colorama.Fore.RESET
        _5 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Run' + ' ' + '-'*20 + colorama.Fore.RESET
        _6 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Input' + ' ' + '-'*20 + colorama.Fore.RESET
        _7 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Output' + ' ' + '-'*20 + colorama.Fore.RESET
        _8 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Stats' + ' ' + '-'*20 + colorama.Fore.RESET
        _9 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'End' + ' ' + '-'*20 + colorama.Fore.RESET
        try:
            print('\n'.join([_1,_2,_3,_4,_5]))
            c = Loading()
            t = threading.Thread(target=c.run, args=("Hệ thống kiểm tra kết quả của bạn", ), daemon=True)
            t.start()
            time.sleep(random.randint(1,3))
            if os.path.isfile(code_or_path):
                with open(code_or_path, encoding='utf-8') as f:
                    code = f.read()
            else:
                code = code_or_path
            c.terminate()
            while threading.active_count() > 1:
                time.sleep(0.1)
            print()
            print(_6)
            print(colorama.Fore.LIGHTCYAN_EX + '> ' + self.custom_input() + colorama.Fore.RESET)
            _error = False
            with self.stdoutIO() as s:
                try:
                    exec(code, {'input': self.custom_input}, globals())
                except Exception as e:
                    _error = True
            if _error:
                try:
                    c.terminate()
                    print()
                except:
                    pass
                print(colorama.Fore.RED + 'Code lỗi' + colorama.Fore.RESET)
                print(_9 + '\n')
                return print(Docs().doitiente())
            print(_7)
            print(colorama.Fore.LIGHTCYAN_EX + '> ' + s.getvalue() + colorama.Fore.RESET)
            # get vnd variable
            vnd = globals()['vnd']
            usd = globals()['usd']
            print(_8)
            if 22*int(usd) == vnd:
                print(colorama.Fore.LIGHTCYAN_EX + 'Code hoàn hảo nha' + colorama.Fore.RESET)
                print(_9)
                return True
            else:
                print(colorama.Fore.RED + 'Code sai nha' + colorama.Fore.RESET)
                print(_9 + '\n')
                return print(Docs().doitiente())
        except Exception as e:
            try:
                c.terminate()
                print()
            except:
                pass
            print(colorama.Fore.RED + 'Code lỗi' + colorama.Fore.RESET)
            print(_9 + '\n')
            return print(Docs().doitiente())
    
    def fakeAI(self, code_or_path) -> str:
        '''
        Kiểm tra mức độ thông minh "AI" của bạn :))
        '''
        _1 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'USD to VND Checker' + ' ' + '-'*20 + colorama.Fore.RESET
        _2 = ''
        _3 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Module' + ' ' + '-'*20 + colorama.Fore.RESET
        _4 = colorama.Fore.LIGHTCYAN_EX + '> Đã load!' + colorama.Fore.RESET
        _5 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Run' + ' ' + '-'*20 + colorama.Fore.RESET
        _6 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Input' + ' ' + '-'*20 + colorama.Fore.RESET
        _7 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Output' + ' ' + '-'*20 + colorama.Fore.RESET
        _8 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Stats' + ' ' + '-'*20 + colorama.Fore.RESET
        _9 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'End' + ' ' + '-'*20 + colorama.Fore.RESET
        
        try:
            print('\n'.join([_1,_2,_3,_4,_5]))
            c = Loading()
            t = threading.Thread(target=c.run, args=("Hệ thống kiểm tra câu trả lời của AI", ), daemon=True)
            t.start()
            time.sleep(random.randint(1,3))
            self.total_dumb = 0
            self.total_smart = 0
            if os.path.isfile(code_or_path):
                with open(code_or_path, 'r', encoding='utf-8') as f:
                    code = f.read()
            else:
                code = code_or_path
            data = open('simple_wordlist.txt', 'r', encoding='utf-8').readlines()
            self.wordlist = []
            for _ in range(1000):
                choiz = random.choice(data)
                self.wordlist.append(choiz)
                data.remove(choiz)
            c.terminate()
            while threading.active_count() > 1:
                time.sleep(0.1)
            print()
            print(_6)
            print(colorama.Fore.LIGHTCYAN_EX + '> 1000 từ ngẫu nhiên từ tệp simple_wordlist.txt' + colorama.Fore.RESET)
            _error = False
            
            with self.stdoutIO() as s:
                try:
                    exec(code, {'input': lambda: self.done(), 'exit': self.no_exit, 'sys.exit': self.no_exit}, globals())
                except:
                    _error = True
            if _error:
                try:
                    c.terminate()
                    while threading.active_count() > 1:
                        time.sleep(0.1)
                    print()
                except:
                    pass
                print(colorama.Fore.RED + 'Code lỗi' + colorama.Fore.RESET)
                print(_9 + '\n')
                return print(Docs().fakeAI())
            splited_data = s.getvalue().split('\n')
            print(_7)
            for line in splited_data:
                if 'robot' in line.lower() or 'máy' in line.lower():
                    print(colorama.Fore.LIGHTCYAN_EX + '> ' + line + colorama.Fore.RESET)
                self.analyze_basic(line)
            
            print(_8)
            print(colorama.Fore.LIGHTCYAN_EX + '> Trả lời được: ' + str(self.total_smart) + colorama.Fore.RESET)
            print(colorama.Fore.LIGHTCYAN_EX + '> Trả lời sai: ' + str(self.total_dumb) + colorama.Fore.RESET)
            print(_9)
        except Exception as e:
            try:
                c.terminate()
                while threading.active_count() > 1:
                    time.sleep(0.1)
                print()
            except:
                pass
            print(colorama.Fore.RED + 'Đã có lỗi xảy ra' + colorama.Fore.RESET)
            print(_9 + '\n')
            return print(Docs().fakeAI())