
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
        _2 = colorama.Fore.LIGHTCYAN_EX + '1. Xác định tỉ giá USD/VND, 1 USD = 22.000 VND' + colorama.Fore.RESET
        _3 = colorama.Fore.LIGHTCYAN_EX + '2. Tính tổng tiền cần chuyển đổi' + colorama.Fore.RESET
        _4 = colorama.Fore.LIGHTCYAN_EX + '3. Tính tổng tiền sau khi chuyển đổi' + colorama.Fore.RESET
        _5 = colorama.Fore.LIGHTCYAN_EX + '4. Hiển thị kết quả' + colorama.Fore.RESET
        _7 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example code' + ' ' + '-'*20 + colorama.Fore.RESET
        _8 = colorama.Fore.LIGHTCYAN_EX + '''
USD = int(input('Nhập số tiền USD: '))
VND = USD * 22000
print('Số tiền sau khi chuyển đổi là: ', VND)
        ''' + colorama.Fore.RESET
        _9 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example Input' + ' ' + '-'*20 + colorama.Fore.RESET
        _10 = colorama.Fore.LIGHTCYAN_EX + '''
Nhập số tiền USD: 100
        ''' + colorama.Fore.RESET
        _11 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + 'Example Output' + ' ' + '-'*20 + colorama.Fore.RESET
        _12 = colorama.Fore.LIGHTCYAN_EX + '''
Số tiền sau khi chuyển đổi là: 2200000
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
        _1 = colorama.Fore.LIGHTGREEN_EX + '-'*20 + ' ' + '"AI" Checker' + ' ' + '-'*20 + colorama.Fore.RESET
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
            data = wordlist().split('\n')
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

### SOMETHING SO BAD


def wordlist():
    return '''a
a dua
a hoàn
a phiến
a tòng
à
ả
ả đào
ả giang hồ
á
á-căn-đình
á khẩu
á khôi
á kim
á rập
ạ
ác
ác cảm
ác chiến
ác mộng
ác nghiệt
ác phụ
ác tà
ác tâm
ác thú
ách
ạch
ai
ai ai
ai điếu
ai oán
ải
ải quan
ái
ái ân
ái hữu
ái khanh
ái lực
ái mộ
ái nam ái nữ
ái ngại
ái nhĩ lan
ái phi
ái quốc
ái tình
am
am hiểu
am pe
ảm đạm
ám
ám ảnh
ám chỉ
ám hại
ám hiệu
ám muội
ám sát
ám tả
ám thị
an
an ba ni
an bài
an cư
an dưỡng
an nghỉ
an ninh
an phận
an táng
an tâm
an toàn
an ủi
an vị
án
án mạng
án ngữ
án phí
án sát
án thư
án tử hình
ang
ang áng
áng
anh
anh ánh
anh dũng
anh đào
anh em
anh hùng
anh linh
anh tài
anh thư
anh tuấn
ảnh
ảnh ảo
ảnh hưởng
ảnh lửa
ánh
ánh đèn
ánh nắng
ánh sáng
ao
ao ước
ào
ào ào
ào ạt
ảo
ảo ảnh
ảo giác
ảo mộng
ảo não
ảo thuật
ảo tưởng
ảo tượng
áo
áo choàng
áo dài
áo giáp
áo gối
áo mưa
áo ngủ
áo quan
áo quần
áo sơ mi
áp
áp bức
áp dụng
áp đảo
áp đặt
áp giải
áp lực
áp suất
áp tải
áp tới
át
au
áy náy
ắc qui
ăm ắp
ẵm
ăn
ăn bám
ăn bận
ăn bốc
ăn bớt
ăn cá
ăn cánh
ăn cắp
ăn chay
ăn chắc
ăn chơi
ăn cỗ
ăn cơm
ăn cơm tháng
ăn cưới
ăn cướp
ăn giải
ăn gian
ăn giỗ
ăn hại
ăn hiếp
ăn hoa hồng
ăn hỏi
ăn hối lộ
ăn không
ăn khớp
ăn kiêng
ăn lãi
ăn lan
ăn lương
ăn mày
ăn nằm
ăn năn
ăn nhịp
ăn nói
ăn ở
ăn quịt
ăn sống
ăn sương
ăn tạp
ăn tết
ăn tham
ăn thề
ăn thua
ăn thử
ăn thừa
ăn tiệc
ăn tiền
ăn tiêu
ăn trộm
ăn uống
ăn vạ
ăn vụng
ăn xén
ăn xổi
ăn ý
ẳng ẳng
ắp
ắt
âm
âm ấm
âm ba
âm cung
âm cực
âm dương
âm đạo
âm điệu
âm giải
âm hạch
âm hành
âm hộ
âm hồn
âm hưởng
âm ỉ
âm lượng
âm mao
âm mưu
âm nang
âm nhạc
âm phủ
âm sắc
âm thầm
âm thần
âm thoa
âm tín
âm u
âm vận
âm vật
ầm
ầm ĩ
ẩm
ẩm thấp
ẩm thực
ấm
ấm áp
ấm chén
ấm cúng
ấm no
ân
ân ái
ân cần
ân hận
ân huệ
ân nghĩa
ân nhân
ân oán
ân tình
ân xá
ẩn
ẩn dật
ẩn náu
ẩn sỉ
ẩn ý
ấn
ấn chỉ
ấn định
ấn hành
ấn loát
ấn quán
ấn tín
ấn tượng
ấp
ấp ủ
ập
âu
âu châu
âu phục
âu sầu
âu yếm
ẩu
ẩu đả
ấu
ấu trĩ
ấu trùng
ấy
ba
ba ba
ba bó một giạ
ba chân bốn cẳng
ba chìm bảy nổi
ba cọc ba đồng ba dò
ba đào
ba gai
ba hoa
ba láp
ba lăng nhăng
ba lê
ba lô
ba phải
ba quân
ba que
ba rọi
ba sinh
ba trợn
ba tư
bà
bà chằng
bà chủ
bà con
bà cụ
bà đỡ
bà phước
bà vãi
bả
bả vai
bã
bá
bá âm
bá cáo
bá chủ
bá hộ
bá láp
bá quan
bá quyền
bá tánh
bá tước
bá vương
bạ
bạ ai
bác
bác ái
bác bẻ
bác cổ
bác học
bác sĩ
bác vật
bạc
bạc ác
bạc hà
bạc hạnh
bạc nghĩa
bạc nhạc
bạc nhược
bạc phận
bạc tình
bách
bách bộ
bách hợp
bách khoa
bách nghệ
bách niên giai lão
bách phân
bách thảo
bách thú
bách tính
bạch
bạch cầu
bạch cúc
bạch cung
bạch dương
bạch đàn
bạch đinh
bạch huyết
bạch kim
bạch lạp
bạch ngọc
bạch tuộc
bạch tuyết
bạch yến
bài
bài bác
bài báo
bài ca
bài diễn văn
bài học
bài làm
bài luận
bài thơ
bài tiết
bài vị
bài xích
bãi
bãi biển
bãi bỏ
bãi chức
bãi cỏ
bãi công
bãi nại
bãi sa mạc
bãi tha ma
bãi trường
bái
bái biệt
bái đáp
bái phục
bái tạ
bái yết
bại
bại hoại
bại lộ
bại sản
bại tẩu
bại trận
bại vong
bám
bám riết
ban
ban ân
ban bố
ban công
ban đầu
ban đêm
ban giám khảo
ban hành
ban khen
ban ngày
ban phát
ban phước
ban thưởng
bàn
bàn bạc
bàn cãi
bàn chải
bàn cờ
bàn giao
bàn mổ
bàn tán
bàn tay
bàn thờ
bàn tính
bàn tọa
bản
bản án
bản cáo trạng
bản chất
bản đồ
bản đồ lưu thông
bản hát
bản in
bản kịch
bản lãnh
bản lề
bản năng
bản ngã
bản quyền
bản sao
bản sắc
bản thảo
bản tính
bản tóm tắt
bản văn
bản vị
bản xứ
bán
bán buôn
bán cầu
bán chịu
bán dạo
bán đảo
bán kết
bán khai
bán kính
bán lẻ
bán nam bán nữ
bán nguyệt
bán nguyệt san
bán niên
bán thân
bán tín bán nghi
bán tự động
bạn
bạn cũ
bạn đọc
bạn đời
bạn học
bạn lòng
bạn thân
bang
bang giao
bang trợ
bang trưởng
bàng
bàng hoàng
bàng quan
bàng thính
bảng
bảng danh dự
bảng đen
bảng hiệu
báng
báng bổ
banh
bành
bành trướng
bành voi
bảnh
bảnh bao
bánh
bánh bao
bánh lái
bánh mì
bánh tráng
bao
bao bì
bao biện
bao bọc
bao dung
bao giấy
bao giờ
bao gồm
bao hàm
bao la
bao lơn
bao nhiêu
bao quanh
bao tay
bao thơ
bao tử
bao vây
bào
bào chế
bào chữa
bào thai
bảo
bảo an
bảo chứng
bảo đảm
bảo hiểm
bảo hòa
bảo hộ
bảo mật
bảo quản
bảo tàng
bảo thủ
bảo trợ
bảo vệ
bão
bão tuyết
báo
báo cáo
báo chí
báo động
báo hiếu
báo hiệu
báo hỷ
báo oán
báo ơn
báo thức
báo trước
báo ứng
bạo
bạo bệnh
bạo chúa
bạo động
bạo hành
bạo lực
bạo ngược
bạo phát
bát
bát âm
bát hương
bát ngát
bát nháo
bạt
bạt đãi
bạt mạng
bạt ngàn
bàu
báu vật
bay
bay bướm
bay hơi
bay lên
bay nhảy
bày
bày biện
bày đặt
bày tỏ
bảy
bắc
bắc bán cầu
bắc cực
băm
bằm vằm
bặm
băn khoăn
bắn
bắn phá
bắn tin
băng
băng bó
băng ca
băng dương
băng điểm
băng hà
băng huyết
băng keo
băng sơn
bằng
bằng an
bằng chứng
bằng hữu
bằng lòng
bẵng
bắp
bắp cải
bắp chân
bắp đùi
bắt
bắt bẻ
bắt bí
bắt bớ
bắt buộc
bắt chước
bắt cóc
bắt đầu
bắt giam
bắt nạt
bắt phạt
bắt rễ
bắt tay
bắt vạ
bặt
bặt tăm
bặt thiệp
bấc
bậc
bầm
bẩm
bẩm sinh
bẩm tính
bấm
bấm bụng
bấm chuông
bần
bần cùng
bần thần
bần tiện
bẩn
bẩn chật
bấn
bận
bận lòng
bâng khuâng
bâng quơ
bấp bênh
bập bẹ
bập bềnh
bất
bất bạo động
bất biến
bất bình
bất chính
bất công
bất diệt
bất đắc chí
bất đắc dĩ
bất định
bất đồng
bất động
bất hạnh
bất hảo
bất hòa
bất hợp lý
bất hợp pháp
bất hủ
bất khuất
bất lợi
bất lực
bất lương
bất ngờ
bất nhân
bất tiện
bất tỉnh
bất trắc
bất tường
bật
bật lửa
bâu
bầu
bầu rượu
bầu tâm sự
bầu trời
bấu
bây
bây bẩy
bây giờ
bầy
bầy hầy
bẩy
bẫy
bấy lâu
bậy
be
be be
bè
bẻ
bẻ vụn
bẽ
bẽ bàng
bé
bé tí
bẹ
bẻm
bèn
bẽn lẽn
bén
bén mảng
bén mùi
bẹn
beo
bèo
bèo bọt
béo
béo bở
bép xép
bẹp
bét
bét nhè
bê
bê tha
bê trễ
bề
bề bộn
bề cao
bề thế
bề trên
bể
bể ái
bể bơi
bể dâu
bễ
bế
bế mạc
bế tắc
bệ
bệ hạ
bệ rạc
bệ vệ
bệch
bên
bên bị
bên nguyên
bền
bền chí
bền vững
bến đò
bến tàu
bến xe
bện
bênh
bênh vực
bềnh bồng
bếp
bếp núc
bết
bệt
bêu
bêu xấu
bệu
bi
bi ai
bi ca
bi đát
bi kịch
bi quan
bi tráng
bì
bì bõm
bỉ
bỉ mặt
bỉ vận
bí
bí ẩn
bí mật.
bí quyết
bí thư
bị
bị chú
bị động
bị lừa
bị thịt
bị thương
bia
bia miệng
bìa
bịa
bích chương
bích ngọc
bịch
biếc
biếm
biếm họa
biên
biên bản
biên giới
biên lai
biên tập
biền biệt
biển
biển lận
biển thủ
biến
biến chất
biến chứng
biến cố
biến động
biến thể
biến thiên
biện bạch
biện chứng
biện hộ
biện minh
biện pháp
biếng
biếng nhác
biết
biết ơn
biết ý
biệt
biệt danh
biệt hiệu
biệt kích
biệt ly
biệt tài
biệt thự
biệt xứ
biểu
biểu diễn
biểu hiện
biểu lộ
biểu ngữ
biểu quyết
biểu tình
biếu
bìm bìm
bím tóc
bịn rịn
binh
binh bị
binh biến
binh chủng
binh lực
binh pháp
binh sĩ
binh xưởng
bình
bình an
bình dân
bình đẳng
bình định
bình luận
bình minh
bình nguyên
bình phục
bình thản
bình thường
bình tĩnh
bỉnh bút
bịnh
bịnh căn
bịnh chứng
bịnh dịch
bịnh học
bịnh nhân
bịnh viện
bịnh xá
bịp
bít
bít tất
bịt
bịt bùng
bìu
bìu dái
bĩu môi
bíu
bò
bò cạp
bò sát
bỏ
bỏ bê
bỏ dở
bỏ đói
bỏ hoang
bỏ lỡ
bỏ phí
bỏ phiếu
bỏ trốn
bỏ tù
bỏ xứ
bõ
bõ công
bõ cơn giận
bó
bó buộc
bó gối
bó lúa
bó thân
bọ
bọ chét
bọ hung
bọ ngựa
bọ rầy
bóc
bóc lột
bóc vảy
bọc
bói
bói cá
bom
bom đạn
bom hóa học
bom khinh khí
bom nguyên tử
bỏm bẻm
bõm
bon bon
bòn
bòn mót
bón
bọn
bong
bong bóng
bong gân
bòng
bõng
bóng
bóng bảy
bóng cá
bóng dáng
bóng đèn
bóng gió
bóng loáng
bóng trăng
bọng đái
boong
bóp
bóp còi
bóp nghẹt
bót
bọt
bọt biển
bô
bô lão
bồ
bồ câu
bồ hóng
bồ liễu
bồ nhìn
bổ
bổ dưỡng
bổ ích
bổ nhiệm
bổ sung
bố
bố cáo
bố cục
bố mẹ
bố trí
bộ
bộ chỉ huy
bộ dạng
bộ điệu
bộ đồ
bộ đội
bộ hạ
bộ hành
bộ lạc
bộ máy
bộ mặt
bộ phận
bộ sách
bốc
bốc cháy
bốc hơi
bốc khói
bốc thuốc
bộc lộ
bộc phát
bôi
bôi bẩn
bôi trơn
bồi
bồi dưỡng
bồi hồi
bồi thường
bổi
bối rối
bội
bội bạc
bội phản
bội tín
bôm
bôn ba
bồn
bồn chồn
bồn hoa
bổn phận
bốn
bốn phương
bộn
bông
bông đùa
bông lông
bông lơn
bồng
bồng bột
bồng lai
bổng
bổng lộc
bỗng
bốp
bộp chộp
bột
bột phát
bơ
bơ phờ
bơ vơ
bờ
bờ bến
bờ biển
bờ đê
bờ sông
bở
bỡ ngỡ
bợ
bơi
bơi ngửa
bơi xuồng
bởi
bởi thế
bới
bới tác
bơm
bờm
bờm xờm
bợm
bỡn cợt
bớt
bu
bù
bù xú
bú
bú dù
bụ
bùa
bùa yêu
búa
bục
bùi
bùi ngùi
bùi nhùi
bụi
bụi bặm
bụm miệng
bùn
bủn rủn
bủn xỉn
bún
bung xung
bùng cháy
bùng nổ
bủng
búng
bụng
bụng nhụng
buộc
buộc tội
buổi
buồm
buôn
buôn lậu
buồn
buồn bực
buồn cười
buồn rầu
buồn thảm
buông
buông tha
buồng
buồng hoa
buồng the
buồng trứng
buốt
buột
buột miệng
búp
búp bê
bút
bút ký
bút pháp
bụt
bư
bự
bừa
bừa bãi
bửa
bữa
bựa
bức
bức bách
bức thư
bức tranh
bực bội
bực tức
bưng
bưng bít
bừng
bứng
bước
bước đường
bước ngoặt
bước tiến
bươi
bưởi
bươm bướm
bướng
bươu
bướu
bướu cổ
bứt
bứt rứt
bưu chính
bưu cục
bưu điện
bưu kiện
bưu phí
bưu tá
bưu thiếp
bưu tín viên
ca
ca bô
ca cao
ca dao
ca khúc
ca kịch
ca kỹ
ca lô
ca ngợi
ca nhạc
ca nô
ca ri
ca rốt
ca trù
ca tụng
ca vũ
cà
cà chua
cà độc dược
cà kheo
cà khịa
cà lăm
cà nhắc
cà phê
cà rá
cà rem
cà sa
cà vạt
cả
cả gan
cả nể
cả ngày
cả quyết
cả thảy
cá
cá biển
cá biệt
cá bống
cá chép
cá con
cá đồng
cá đuối
cá gỗ
cá hộp
cá kho
cá mập
cá mè
cá mòi
cá muối
cá ngựa
cá nhân
cá ông
cá sấu
cá thể
cá thu
cá tính
cá trê
cá tươi
cá ươn
cạ
các
cách
cách biệt
cách cấu tạo
cách chức
cách ly
cách mạng
cách mạng xã hội
cách ngôn
cách thức
cai
cai quản
cai thần
cai thợ
cai trị
cài
cài cửa
cải
cải biên
cải cách
cải chính
cải dạng
cải danh
cải hóa
cải hối
cải táng
cải tạo
cải tiến
cải tổ
cải tử hoàn sinh
cãi
cãi bướng
cãi lộn
cái
cái ghẻ
cái thế anh hùng
cam
cam chịu
cam đoan
cam kết
cam lòng
cam phận
cam thảo
cam tuyền
cảm
cảm động
cảm giác
cảm hóa
cảm hoài
cảm hứng
cảm mến
cảm phục
cảm quan
cảm thấy
cảm tình
cảm tử
cảm tưởng
cảm ứng
cảm xúc
cám
cám cảnh
cám dỗ
cám ơn
cạm bẫy
can
can án
can chi
can đảm
can phạm
can qua
can thiệp
can trường
càn
càn quét
càn rỡ
cản
cản trở
cán
cán bộ
cán cân
cán chổi
cán sự
cán viết
cạn
càng
cảng
cáng
cáng đáng
canh
canh cánh
canh gác
canh giữ
canh khuya
canh nông
canh tác
canh tân
canh tuần
cành
cành nanh
cảnh
cảnh báo
cảnh binh
cảnh cáo
cảnh giác
cảnh huống
cảnh ngộ
cảnh sát
cảnh sắc
cảnh tỉnh
cảnh tượng
cánh
cánh bèo
cánh cửa
cánh đồng
cánh khuỷ
cánh mũi
cánh quạt gió
cánh sinh
cánh tay
cạnh
cạnh khóe
cạnh tranh
cao
cao áp
cao bay xa chạy
cao bồi
cao cả
cao cấp
cao cường
cao danh
cao đẳng
cao độ
cao hứng
cao kiến
cao lâu
cao lương
cao ly
cao minh
cao ngạo
cao nguyên
cao quý
cao siêu
cao su
cao tăng
cao thế
cao thủ
cao thượng
cao ủy
cao vọng
cao xạ
cào
cào cào
cảo bản
cáo
cáo biệt
cáo bịnh
cáo cấp
cáo chung
cáo giác
cáo lỗi
cáo mật
cáo phó
cáo thị
cáo tội
cáo trạng
cáo từ
cạo
cạo giấy
cáp
cạp
cạp chiếu
cát
cát cánh
cát hung
cát tường
cạt tông
cau
cau có
cau mày
càu nhàu
cáu
cáu kỉnh
cáu tiết
caught
cay
cay đắng
cay độc
cay nghiệt
cày
cày bừa
cày cấy
cáy
cạy
cạy cửa
cắc kè
cặc
căm
căm căm
căm hờn
căm thù
cằm
cắm trại
cặm
cặm cụi
căn
căn bản
căn cơ
căn cứ
căn cước
căn dặn
căn nguyên
căn tính
căn vặn
cằn cỗi
cằn nhằn
cắn
cắn câu
cắn cỏ
cắn răng
cắn rứt
cắn xé
cặn
cặn bã
cặn kẽ
căng
căng thẳng
cẳng
cẳng tay
cắng đắng
cắp
cặp
cặp bến
cặp đôi
cặp kè
cặp vợ chồng
cắt
cắt bỏ
cắt bớt
cắt cứ
cắt đặt
cắt may
cắt ngang
cắt nghĩa
cắt thuốc
cắt xén
câm
câm họng
cầm
cầm ca
cầm cái
cầm canh
cầm cập
cầm chắc
cầm chừng
cầm cự
cầm đầu
cầm giữ
cầm lái
cầm lòng
cầm máu
cầm quyền
cầm sắt
cầm thú
cầm tù
cẩm
cẩm chướng
cẩm lai
cẩm nang
cẩm nhung
cẩm thạch
cẩm tú
cấm
cấm chỉ
cấm cố
cấm cửa
cấm dán giấy
cấm địa
cấm khẩu
cấm kỵ
cấm lịnh
cấm thành
cấm vào
cấm vận
cân
cân bàn
cân bằng
cân đối
cân não
cân nhắc
cân xứng
cần
cần cù
cần kiệm
cần kíp
cần mẫn
cần thiết
cần vụ
cần xé
cẩn
cẩn bạch
cẩn mật
cẩn thẩn
cấn
cấn thai
cận
cận chiến
cận đại
cận thị
cận vệ
cấp
cấp báo
cấp bằng
cấp cứu
cấp dưỡng
cấp hiệu
cấp thời
cấp tiến
cập kê
cất
cất đi
cất giấu
cất hàng
cất nhà
cất nhắc
cất tiếng
cật
cật lực
cật một
cật vấn
câu chấp
câu chuyện
câu đố
câu đối
câu hỏi
câu lạc bộ
câu thúc
cầu
cầu an
cầu cạnh
cầu chì
cầu chứng
cầu cứu
cầu hôn
cầu nguyện
cầu thủ
cầu tiêu
cầu tự
cầu vồng
cầu xin
cẩu
cẩu thả
cấu
cấu tạo
cấu thành
cậu
cây
cây cỏ
cây còi
cây dù
cây nến
cây số
cây viết
cây xăng
cấy
cậy
cậy thế
cha
cha đỡ đầu
cha ghẻ
cha mẹ
cha sở
chà
chà là
chà xát
chả
chả giò
chác
chạch
chai
chài
chải
chải chuốt
chải đầu
chàm
chạm
chạm trán
chan chứa
chán
chán ghét
chán nản
chán vạn
chạn
chang chang
chàng
chàng hảng
chàng hiu
chạng vạng
chanh
chanh chua
chánh
chánh án
chánh phạm
chạnh lòng
chao
chào
chào mời
chảo
chão
cháo
chạo
chạp
chát
chát tai
chau mày
cháu
cháu chắt
chay
chày
chảy
chảy máu
chảy rửa
cháy
cháy túi
chạy
chạy chọt
chạy chữa
chạy đua
chạy mất
chạy thoát
chắc
chắc mẩm
chắc nịch
chăm
chăm chú
chăm nom
chăm sóc
chằm
chằm chằm
chặm
chăn
chăn gối
chăn nuôi
chẵn
chắn
chắn bùn
chắn xích
chăng
chăng lưới
chăng màn
chằng
chằng chịt
chẳng
chẳng bõ
chẳng hạn
chẳng may
chẳng những
chẳng thà
chặng
chắp
chắp nhặt
chặp
chắt
chắt bóp
chặt
chặt chẽ
châm
châm biếm
châm ngôn
chấm
chấm dứt
chấm phá
chậm
chậm chạp
chậm tiến
chân
chân dung
chân lý
chân tài
chân thành.
chân tình
chân trời
chân tướng
chần
chần chừ
chẩn
chẩn bịnh
chẩn mạch
chẩn y viện
chấn áp
chấn chỉnh
chấn động
chấn hưng
chận
chận đứng
chấp
chấp chính
chấp hành
chấp nhận
chấp thuận
chập choạng
chập chờn
chập chững
chất
chất chứa
chất độc
chất khí
chất kích thích
chất phác
chất vấn
chật
chật vật
châu
châu báu
châu chấu
châu thổ
chầu
chầu chực
chầu trời
chậu
chầy
chấy
che
che chở
che đậy
che phủ
chè
chè chén
chẻ
chẻ hoe
ché
chém
chém giết
chen
chen chúc
chèn
chèn ép
chẽn
chén
chén cơm
cheo
cheo cưới
cheo leo
chèo
chèo chống
chéo
chéo áo
chép
chẹt
chê
chê bai
chê cười
chế
chế biến
chế độ
chế giễu
chế ngự
chế nhạo
chế tác
chế tạo
chếch
chếch choáng
chêm
chễm chệ
chênh
chênh lệch
chênh vênh
chểnh mảng
chệnh choạng
chết
chết đuối
chết giấc
chết tươi
chi
chi bằng
chi đoàn
chi phí
chi phiếu
chi phối
chi tiết
chì
chỉ
chỉ đạo
chỉ định
chỉ huy
chỉ rõ
chỉ tay
chỉ thị
chỉ trích
chí
chí ác
chí chết
chí công
chí hiếu
chí hướng
chí khí
chí lý
chí tuyến
chí yếu
chị
chị bộ
chia
chia lìa
chia ly
chìa
chìa khóa
chĩa
chích
chích ngừa
chiếc
chiếc bóng
chiêm
chiêm bái
chiêm bao
chiêm ngưỡng
chiếm
chiếm đoạt
chiếm giữ
chiên
chiến
chiến bại
chiến bào
chiến binh
chiến dịch
chiến đấu
chiến hào
chiến hữu
chiến khu
chiến lược
chiến sĩ
chiến thắng
chiến thuật
chiến tranh
chiến trận
chiến trường
chiêng
chiết
chiết khấu
chiết quang
chiết trung
chiết tự
chiêu
chiêu bài
chiêu đãi
chiêu mộ
chiều
chiều chuộng
chiều ý
chiếu
chiếu chỉ
chiếu cố
chiếu khán
chiếu lệ
chim
chim chuột
chim muông
chim xanh
chìm
chín
chín chắn
chín mối
chín nhừ
chỉnh
chỉnh lý
chĩnh
chíp
chít
chít khăn
chịt
chịu
chịu đầu hàng
chịu khó
chịu nhục
chịu tang
chịu thua
chịu tội
cho
cho biết
cho mượn
cho phép
chõ
chó
chó chết
chó sói
chóa mắt
choạc
choán
choàng
choảng
choáng
choáng óc
choáng váng
choắc
chọc
chọc ghẹo
chọc giận
chóe
chòi
chòi canh
chõi
chói
chói mắt
chọi
chòm
chỏm
chọn
chọn lọc
chong
chong chóng
chòng chành
chòng chọc
chòng ghẹo
chõng
chóng
chóng vánh
chóp chóp
chót
chót vót
chỗ
chốc
chốc nữa
chồi
chồi rễ
chổi
chối
chối từ
chồm
chôn
chồn
chốn
chông
chông gai
chồng
chồng ngồng
chổng
chổng gọng
chống
chống chế
chống chỏi
chống trả
chốp
chộp
chốt
chột dạ
chột mắt
chờ
chờ chết
chờ xem
chở
chở khách
chớ
chợ
chợ trời
chơi
chơi ác
chơi bời
chơi chữ
chơi đĩ
chới với
chơm chởm
chớm
chớm nở
chờn vờn
chớp
chớp mắt
chớp nhoáng
chớt nhả
chợt
chợt nhớ
chu cấp
chu đáo
chu kỳ
chu vi
chủ
chủ bút
chủ đề
chủ lực
chủ mưu
chủ nghĩa
chủ nhiệm
chủ quan
chủ quyền
chủ tịch
chủ trì
chủ trương
chủ yếu
chú
chú giải
chú ý
chua
chua cay
chua xót
chùa
chúa
chuẩn
chuẩn bị
chuẩn đích
chuẩn xác
chuẩn y
chúc
chúc mừng
chúc thư
chúc từ
chục
chui
chùi
chúi
chum
chùm
chùm hoa
chụm
chùn
chùn chụt
chung
chung cuộc
chung kết
chung thủy
chung tình
chùng
chủng
chủng đậu
chủng loại
chủng viện
chúng
chúng nó
chúng sinh
chuốc
chuộc
chuộc tội
chuôi
chuỗi
chuỗi ngày
chuối
chuôm
chuồn
chuồn chuồn
chuông
chuông cáo phó
chuồng
chuồng trại
chuồng xí
chuộng
chuốt
chuột
chuột rút
chụp
chụp ảnh
chụp lấy
chút
chút đỉnh
chùy
chuyên
chuyên cần
chuyên chính
chuyên gia
chuyên trách
chuyền
chuyển
chuyển dịch
chuyển động
chuyển hướng
chuyển tiếp
chuyến
chuyến bay
chuyến trước
chuyện
chuyện phiếm
chuyện tình
chư hầu
chư tướng
chừ
chữ
chữ cái
chữ hán
chữ ký
chữ tắt
chữ trinh
chứ
chưa
chưa bao giờ
chừa
chửa
chửa hoang
chữa
chữa bịnh
chứa
chứa chan
chứa đựng
chức
chức nghiệp
chức quyền
chức vụ
chực
chực sẵn
chửi
chửi thề
chưng
chưng bày
chưng hửng
chừng
chừng mực
chững chạc
chứng
chứng bịnh
chứng chỉ
chứng kiến
chứng minh
chứng nhân
chứng nhận
chứng thư
chước
chương
chương trình
chường
chưởng ấn
chưởng khế
chưởng lý
chướng
chướng ngại
chướng tai
co
co bóp
co giãn
co rút
cò
cò mồi
cỏ
cỏ khô
có
có ăn
có chồng
có chửa
có hiếu
có ích
có lẽ
có lý
có nghĩa
có thể
có vẻ
cọ
cọ xát
cóc
cọc
cọc cằn
cọc chèo
coi
coi chừng
coi rẻ
còi
còi xương
cõi
cõi đời
cõi trên
cói
còm
con
con bạc
con bịnh
con cờ
con điếm
con đỡ đầu
con hoang
con ma
con ngươi
con ở
con số
con thú
con tin
con vụ
còn
còn nữa
còn trinh
cỏn con
cong
cong queo
còng
còng cọc
cõng
cóng
cọng
cóp
cọp
cót két
cọt kẹt
cọt xê
cô
cô dâu
cô đơn
cô hồn
cô lập
cô nhi
cô quả
cô quạnh
cô thôn
cổ
cổ điển
cổ động
cổ học
cổ hủ
cổ mộ
cổ nhân
cổ phần
cổ phiếu
cổ tích
cổ truyền
cổ trướng
cổ võ
cỗ
cỗ quan tài
cố
cố chấp
cố định
cố đô
cố gắng
cố hương
cố hữu
cố nhân
cố quốc
cố sát
cố tri
cố vấn
cốc
cộc
cộc cằn
cộc lốc
côi cút
cồi
cỗi
cối
cối xay
cội
cồm cộm
cốm
cộm
côn
côn đồ
côn trùng
cồn
cồn cát
công
công an
công bố
công chính
công chúa
công chúng
công danh
công dân
công đoàn
công giáo
công hàm
công ích
công khai
công luân
công luận
công lực
công lý
công nghệ
công nghiệp
công nhân
công nhận
công pháp
công quĩ
công tác
công thức
công thương
công trái
công ty
công văn
công xã
công xuất
công xưởng
cồng
cồng kềnh
cổng
cống
cống hiến
cộng
cộng hòa
cộng sản
cộng tác
cốt
cốt nhục
cốt truyện
cột
cột cờ
cột trụ
cơ
cơ bản
cơ cực
cơ giới
cơ hội
cơ mưu
cơ nghiệp
cơ quan
cơ sở
cơ thể
cờ
cờ bạc
cờ tướng
cỡ
cớ
cơi
cởi
cởi mở
cơm
cơm đen
cơm nước
cơn mưa
cợt
cu
cu li
cù
cù lao
củ
củ soát
củ vấn
cũ
cú
cú pháp
cú vọ
cụ
cụ thể
cua
của
của cải
của hối lộ
của lạ
cúc
cúc dục
cục
cục diện
cục mịch
cục tẩy
cùi
cùi chỏ
củi
cũi
cúi
cùm
cúm
cúm núm
cụm
cun cút
cùn
cung
cung cầu
cung khai
cung nữ
cung phi
cùng
cùng khổ
cùng tận
củng
củng cố
cũng
cúng
cuộc
cuộc đời
cuồi
cuối
cuối cùng
cuội
cuỗm
cuồn cuộn
cuốn
cuốn gói
cuộn
cuồng
cuồng nhiệt
cuồng tín
cuống
cuống cuồng
cúp
cụp
cút
cụt
cụt hứng
cư
cư dân
cư xử
cử
cử hành
cử nhân
cử tri
cữ
cứ
cứ điểm
cự
cự tuyệt
cưa
cửa
cửa ải
cửa hàng
cửa mình
cửa sổ
cứa
cựa
cực
cực điểm
cực hình
cưng
cứng
cứng cỏi
cước
cước phí
cười
cười chê
cười gượng
cười ngạo
cười tình
cưới
cườm
cương
cương lĩnh
cương quyết
cương trực
cường
cường đạo
cường độ
cường quốc
cường tráng
cưỡng
cưỡng bức
cưỡng dâm
cưỡng đoạt
cướp
cướp biển
cứt
cứt đái
cứt ráy
cứt xu
cưu
cưu mang
cừu
cừu địch
cừu hận
cửu
cửu chương
cửu tuyền
cứu
cứu cánh
cứu tinh
cứu trợ
cứu xét
cựu
cựu chiến binh
cựu kháng chiến
cựu thời
cựu trào
cựu truyền
da
da bọc qui đầu
da cam
da che mắt ngựa
da dẻ
da diết
da láng
da liễu
da mồi
da người
da thịt
da thuộc
dã
dã cầm
dã chiến
dã dượi
dã man
dã nhân
dã tâm
dã thú
dã tràng
dạ
dạ dày
dạ hội
dạ quang
dạ vũ
dạ yến
dai
dai dẳng
dài
dài dòng
dải
dải đất
dãi
dái
dại
dại dột
dám
dạm
dạm bán
dạm vợ
dan díu
dàn
dàn cảnh
dàn hòa
dàn xếp
dán
dạn
dạn mặt
dang
dang dở
dáng
dáng điệu
dạng
danh
danh dự
danh hiệu
danh lam
danh lợi
danh mục
danh nghĩa
danh ngôn
danh phẩm
danh phận
danh sách
danh thiếp
danh từ
danh vọng
dành
dành dành
dành giật
dành riêng
dao
dao cạo
dao động
dao găm
dao mổ
dao xếp
dạo
dạo ấy
dát
dạt
day
dày
dày đặc
dãy
dạy
dạy bảo
dạy tư
dăm
dằm
dặm
dặm trường
dằn
dằn lòng
dặn
dặn bảo
dằng
dằng co
dằng dặc
dắt
dắt díu
dâm
dâm bụt
dâm dật
dâm đãng
dâm loạn
dâm ô
dâm phụ
dâm thư
dầm
dầm dề
dân
dân biểu
dân ca
dân chủ
dân chúng
dân công
dân cư
dân luật
dân quân
dân quê
dân quyền
dân sinh
dân sự
dân tị nạn
dân tộc
dân vận
dần
dần dần
dẫn
dẫn chứng
dẫn dầu
dẫn điện
dẫn đô
dẫn nhiệt
dẫn thủy nhập điền
dấn
dâng
dấp
dập
dập dềnh
dập dìu
dật
dật dục
dật sĩ
dật sử
dâu
dâu cao su
dâu gia
dầu
dầu cá
dầu hắc
dầu hỏa
dầu mỏ
dầu phọng
dầu thơm
dầu thực vật
dấu
dấu chấm
dấu chấm phẩy
dấu chấm than
dấu chân
dấu cộng
dấu hiệu
dấu nặng
dấu ngã
dấu ngoặc
dấu phẩy
dấu sắc
dấu tay
dấu thánh giá
dấu vết
dây
dây cáp
dây chuyền
dây cương
dây dưa
dây giày
dây kẽm gai
dây leo
dây lưng
dây tây
dây xích
dẫy dụa
dấy
dấy binh
dấy loạn
dậy
dậy men
dậy thì
dè
dè dặt
dè xẻn
dẻ
dẻo
dẻo dai
dẻo sức
dép
dẹp
dẹp loạn
dẹp tan
dê
dê cụ
dể ngươi
dễ
dễ bảo
dễ bể
dễ chịu
dễ coi
dễ dãi
dễ dàng
dễ ghét
dễ thương
dế
dệt
dệt gấm
di
di bút
di chúc
di chuyển
di cư
di dân
di động
di hài
di họa
di sản
di tích
di trú
di truyền
di vật
dì
dì ghẻ
dì phước
dỉ
dĩ
dĩ nhiên
dĩ vãng
dí nát
dị
dị chất
dị chủng
dị dạng
dị đoan
dị kỳ
dị nghị
dị nhân
dị thường
dị vật
dĩa
dĩa bay
dịch
dịch giả
dịch hạch
dịch tả
dịch tễ
diệc
diêm
diêm đài
diêm vương
diễm lệ
diễm phúc
diễm tình
diễn
diễn dịch
diễn đàn
diễn đạt
diễn giả
diễn giải
diễn tả
diễn thuyết
diễn văn
diễn viên
diện
diện mạo
diện tích
diện tiền
diệt
diệt chủng
diệt khuẩn
diệt vong
diều
diều hâu
diễu binh
diệu
diệu vợi
dìm
dinh
dinh dưỡng
dinh điền
dính
dính dáng
dịp
dìu
dìu dắt
dìu dặt
dịu
dịu dàng
do
do dự
do thái
do thám
dò
dò hỏi
dò xét
dọa
dọa nạt
doanh
doanh lợi
doanh nghiệp
doanh trại
dóc
dọc
dọc đường
doi
dõi
dom
dòm
dòm chừng
dòm ngó
dòn
dọn
dọn đường
dọn sạch
dong dỏng
dòng
dòng họ
dòng nước
dõng dạc
dỗ
dỗ ngọt
dốc
dốc chí
dồi
dồi dào
dối
dối trá
dội
dồn
dồn dập
dông
dông dài
dộng
dốt
dốt đặc
dột
dơ
dơ dáng
dở
dở hơi
dở ra
dỡ
dớ dẩn
dơi
dời
dợn
dớp
du
du côn
du dương
du đãng
du hành
du khách
du kích
du lịch
du mục
du ngoạn
du thuyền
du xuân
dù
dụ
dụ dỗ
dua nịnh
dục
dục tình
dục vọng
dùi
dùi cui
dụi tắt
dun rủi
dung dị
dung dịch
dung hòa
dung nhan
dung thân
dung thứ
dung túng
dùng
dùng dằng
dũng
dũng cảm
dũng mãnh
dũng sĩ
dụng
dụng cụ
dụng ý
duỗi
duy
duy nhứt
duy tân
duy trì
duy vật
duyên
duyên cớ
duyên hải
duyên kiếp
duyệt
duyệt binh
duyệt y
dư
dư âm
dư giả
dư luận
dữ
dữ kiện
dữ tợn
dứ
dự
dự án
dự định
dự đoán
dự thi
dự toán
dự trù
dưa
dưa hấu
dưa leo
dừa
dứa
dựa
dựa trên
dưng
dừng
dừng lại
dửng dưng
dửng mỡ
dựng
dựng đứng
dược
dược học
dược liệu
dược sĩ
dưới
dương
dương bản
dương cầm
dương lịch
dương liễu
dương tính
dương vật
dường
dường nào
dưỡng
dưỡng bịnh
dưỡng đường
dưỡng sinh
dượng
dượt
dứt
dứt khoát
dứt tình
đa
đa âm
đa bào
đa cảm
đa dâm
đa diện
đa dục
đa giác
đa hôn
đa mang
đa mưu
đa nghi
đa nguyên
đa sầu
đa số
đa thần giáo
đa thê
đa thức
đa tình
đà
đà điểu
đả
đả đảo
đả kích
đả thương
đã
đã đành
đã lâu
đá
đá bóng
đá hoa
đá hoa cương
đá lửa
đá mài
đá vàng
đá vôi
đạc
đạc điền
đai
đài
đài kỷ niệm
đài thọ
đãi
đãi ngộ
đái
đái dầm
đại
đại chiến
đại chúng
đại cương
đại diện
đại hạn
đại học
đại lục
đại ý
đam mê
đàm đạo
đàm luận
đàm phán
đàm thoại
đảm
đảm bảo
đảm đương
đảm nhận
đám
đám cháy
đám cưới
đám ma
đạm
đạm bạc
đan
đàn
đàn áp
đàn bà
đàn bầu
đàn hồi
đàn ông
đản
đạn
đạn dược
đạn đạo
đang
đảng
đảng bộ
đáng
đáng kể
đáng sợ
đành lòng
đánh
đánh bại
đánh bạn
đánh bóng
đánh đổi
đánh đu
đánh đuổi
đánh giá
đánh lừa
đánh thuế
đánh thức
đánh vần
đao
đào
đào binh
đào hoa
đào ngũ
đào tạo
đảo
đảo chánh
đảo điên
đảo ngược
đáo
đáo lý
đạo
đạo đức
đạo luật
đạo nghĩa
đáp
đáp lễ
đạp
đạp đổ
đạt
đau
đau buồn
đau đớn
đau khổ
đau lòng
đay
đay nghiến
đày
đày đọa
đáy
đắc chí
đắc thắng
đắc tội
đặc
đặc biệt
đặc phái viên
đặc tính
đắm
đắm đuối
đẵn
đắn đo
đăng
đăng cai
đăng ký
đăng quang
đăng ten
đằng
đẳng
đẳng áp
đẳng cấp
đẳng thức
đẳng trương
đắng
đắp
đắp đập
đắt
đặt
đặt tên
đâm
đâm liều
đầm
đầm ấm
đầm lầy
đẫm
đấm
đấm bóp
đậm
đậm đà
đần
đập
đất
đất bồi
đất liền
đâu
đầu
đầu bếp
đầu cơ
đầu đảng
đầu đề
đầu độc
đầu phiếu
đấu
đấu bò
đấu giá
đấu khẩu
đấu lý
đấu tranh
đấu trường
đậu
đậu cô ve
đậu đũa
đậu khấu
đậu mùa
đậu nành
đậu phụ
đây
đầy
đầy ắp
đầy dẫy
đầy đủ
đẩy
đẩy ngã
đẫy
đấy
đậy
đe
đe dọa
đè
đè nén
đẻ
đem
đem lại
đem về
đen
đen tối
đèn
đèn điện
đèn ống
đèn pin
đèn vách
đèn xếp
đèn xì
đeo
đeo đuổi
đèo
đèo bồng
đẽo
đẹp
đẹp lòng
đẹp mắt
đét
đê hèn
đề
đề cử
đề nghị
đề phòng
để
để dành
để ý
đế quốc
đế vương
đệ đơn
đệ trình
đệ tử
đêm
đêm nay
đêm ngày
đếm
đệm
đền
đền tội
đến
đến tuổi
đều
đều nhau
đểu
đi
đi bộ
đi chơi
đi dạo
đi làm
đi ngủ
đi trốn
đi vắng
đì
đĩ
đìa
địa
địa cầu
địa chỉ
địa đạo
địa điểm
địa lý học
địa ngục
địa tầng
địa vị
đích
đích danh
đinh
đinh ốc
đình
đình chiến
đình công
đỉnh
đĩnh
đính
đính hôn
định
định bụng
định cư
định hướng
định luật
định lý
định mạng
định nghĩa
định tính
định vị
đít
địt
đìu hiu
đo
đo ván
đò
đỏ
đỏ tươi
đó
đọ
đọa đày
đoái tưởng
đoan
đoan chính
đoàn
đoàn kết
đoàn thể
đoàn tụ
đoàn viên
đoản kiếm
đoán
đoán trước
đoạn
đoạn trường
đoạn tuyệt
đoạt
đoạt chức
đọc
đòi
đòi tiền
đói
đọi
đom đóm
đòn
đòn cân
đòn dông
đòn tay
đón
đón tiếp
đong
đóng
đóng khung
đóng thuế
đọng
đọt
đô hộ
đô thị
đô vật
đồ
đồ ăn
đồ bỏ
đồ chơi
đồ đạc
đồ nghề
đồ tể
đổ
đổ máu
đỗ
đỗ quyên
đố
độ
độ thân
đốc công
độc
độc giả
độc hại
độc lập
độc nhất
độc tài
độc thân
đôi
đôi co
đôi khi
đồi
đồi bại
đổi
đổi chác
đổi thay
đổi tiền
đỗi
đối
đối diện
đối lập
đối ngoại
đối nội
đối phó
đội
đốm
đồn
đồn trú
đốn
độn
độn thổ
độn vai
đông
đông đảo
đông đúc
đông y
đồng
đồng âm
đồng bộ
đồng chí
đồng lõa
đồng nghĩa
đồng tiền
đồng tử
đồng vị
đồng ý
đống
động
động cơ
động đào
động đất
động tác
động vật
động viên
đốt
đột
đột kích
đột xuất
đờ
đờ đẫn
đỡ
đỡ đầu
đợ
đời
đời đời
đời nào
đời sống
đới
đợi
đờm
đơn
đơn sơ
đơn vị
đớn hèn
đớp
đợt
đu
đu đưa
đủ
đủ ăn
đụ
đua
đua đòi
đùa
đùa cợt
đùa nghịch
đũa
đúc
đúc kết
đục
đui
đùi
đùm
đun
đụn
đúng
đúng giờ
đụng
đuốc
đuôi
đuổi
đuổi kịp
đuổi theo
đúp
đút
đút lót
đụt mưa
đưa
đưa đón
đưa đường
đưa tin
đưa tình
đứa bé
đức tính
đực
đừng
đứng
đứng vững
đứng yên
đựng
được
được quyền
đười ươi
đương chức
đương cục
đương đầu
đương nhiên
đường
đường bộ
đường cấm
đường đời
đường trường
đường về
đứt
đứt tay
e
e dè
e lệ
e ngại
e rằng
è cổ
em
em chồng
em dâu
em gái
em họ
ém
ém nhẹm
én
eo
eo biển
eo đất
eo éo
eo hẹp
eo lưng
èo uột
ẻo lả
ẽo ẹt
éo le
ẹo
ép
ép buộc
ép duyên
ép liễu nài hoa
ép lòng
ép nài
ép uổng
ẹp
ê
ê a
ê ẩm
ê chề
ê hề
ê răng
ề à
ế
ế chồng
ếch
ếch nhái
êm
êm ả
êm ái
êm ấm
êm dịu
êm đềm
êm tai
êm thấm
ếm
ềnh
ễnh
ễnh ương
ga
ga ra
ga tô
gà
gà chọi
gà đồng
gà giò
gà lôi
gà mái
gà mái ghẹ
gà mờ
gà rừng
gà tây
gà thiến
gà trống
gả
gã
gá
gạ
gạ gẫm
gác
gác bỏ
gác chuông
gác dan
gác lửng
gác xép
gạc
gạch
gạch đít
gạch nối
gạch ống
gai
gai góc
gai mắt
gai ốc
gài
gài bẫy
gài cửa
gãi
gái
gái điếm
gái giang hồ
gái góa
gái nhảy
gái tơ
gain
gan
gan bàn chân
gan dạ
gan góc
gan lì
gàn
gán
gạn cặn
gạn hỏi
gang
ganh đua
ganh ghét
gánh
gánh hát
gào
gào thét
gáo
gạo
gạo nếp
gạt
gạt lệ
gạt nợ
gàu
gàu ròng
gay cấn
gay gắt
gay go
gảy đàn
gãy
gãy đổ
gáy
gáy sách
găm
gặm
gặm nhấm
gắn
gắn bó
gắn liền
găng
gắng
gắng sức
gắp
gặp
gặp gỡ
gặp may
gặp mặt
gặp nạn
gặp nhau
gắt
gắt gỏng
gặt
gầm
gầm ghè
gầm thét
gẫm
gấm
gân
gân cốt
gần
gần đây
gần gũi
gần xa
gấp
gấp bội
gấp đôi
gấp khúc
gập ghềnh
gật
gấu
gấu chó
gấu mèo
gấu ngựa
gây
gây dựng
gây nợ
gây sự
gây thù
gầy
gầy còm
gầy đét
gầy gò
gầy guộc
gầy yếu
gậy
ghe
ghè
ghẻ
ghẻ lạnh
ghé
ghẹ
ghen
ghen ghét
ghen tỵ
ghẹo
ghép
ghét
ghê
ghê tởm
ghế
ghế bành
ghế dài
ghế đẩu
ghế điện
ghếch
ghềnh
ghi
ghi âm
ghi chép
ghi nhập
ghi nhớ
ghì
ghiền
ghim
ghìm
gì
gỉ
gia
gia cảnh
gia công
gia đình
gia nhập
gia phả
gia sản
gia súc
gia tài
gia tăng
gia tốc
gia truyền
gia vị
già
già dặn
già lam
giả
giả bộ
giả danh
giả dối
giả định
giả mạo
giả sử
giả thuyết
giã
giã độc
giã từ
giá
giá buốt
giá cả
giá chợ đen
giá thị trường
giạ
giác
giác mạc
giác ngộ
giác quan
giác thư
giai âm
giai cấp
giai đoạn
giai nhân
giải
giải cứu
giải khát
giải khuây
giải nghĩa
giải nhiệt
giải pháp
giải phẫu
giải phóng
giải quyết
giải tán
giải thể
giải thích
giải tỏa
giải trí
giãi bày
giam
giảm
giảm nhẹ
giảm sút
giảm thuế
giảm tội
giám định
giám đốc
giám khảo
giám mục
giám ngục
giám sát
giám thị
giạm
gian
gian dâm
gian dối
gian xảo
giàn
giản dị
giản lược
giản tiện
giãn
gián
gián điệp
gián tiếp
giang
giang hồ
giang mai
giang sơn
giảng
giảng đường
giảng giải
giảng sư
giáng
giáng sinh
giành
giao
giao cấu
giao chiến
giao dịch
giao hợp
giao hưởng
giao hữu
giao phó
giao thiệp
giao thông
giao thời
giao thừa
giảo
giảo quyệt
giáo
giáo án
giáo cụ
giáo dân
giáo dục
giáo đầu
giáo điều
giáo đường
giáo hoàng
giáo khoa
giáo phái
giáo sĩ
giáo sinh
giáo sư
giáo viên
giáp
giáp mặt
giàu
giày
giày vò
giãy
giãy chết
giặc
giặc biển
giặc cướp
giặc giã
giẵm
giặm
giằn
giằn vặt
giăng
giăng lưới
giằng
giằng co
giắt
giặt
giấc
giấc mơ
giấc ngủ
giâm
giầm
giấm
giậm
giần
giận
giận dữ
giập
giật
giật gân
giật lùi
giấu
giậu
giây
giấy
giấy bạc
giấy biên lai
giấy chứng chỉ
giấy dầu
giấy in
giấy khai sanh
giấy khai tử
giấy má
giấy phép
giấy than
giấy thông hành
giấy vệ sinh
giẻ
gièm
gieo
gieo rắc
giẹo
giẹp
giền
giêng
giếng
giết
giết hại
giết thịt
giễu
giễu cợt
gìn
gìn giữ
giò
giỏ
gió
gió bảo
gió lốc
gió lùa
gió mùa
gió nồm
gióc
giòi
giỏi
giọi
giòn
giong
giong ruổi
giỏng
giỏng tai
gióng
giọng
giọng kim
giọng lưỡi
giọng nói
giọng thổ
giọt
giọt máu
giọt mưa
giọt nước
giọt sương
giỗ
giồi
giội
giống
giống loài
giống người
giống nòi
giơ
giờ
giờ đây
giờ giấc
giờ làm thêm
giờ phút
giờ rãnh
giới
giới hạn
giới thiệu
giới tính
giới từ
giờn
giởn tóc gáy
giỡn
giũ
giũa
giục
giùi
giúi
giụi mắt
giun
giun đất
giun đũa
giun kim
giúp
giúp ích
giữ
giữ chỗ
giữ kín
giữ lời
giữ sức khỏe
giữ trật tự
giữa
giữa trưa
giương
giương buồm
giương mắt
giường
giựt
giựt mình
go
gò
gò bó
gò má
gõ
góa
góa bụa
góc
gỏi
gói
gọi
gọi điện thoại
gom
gòn
gọn gàng
gọng
góp
góp mặt
góp nhặt
góp phần
góp sức
góp vốn
gót
gọt
gồ
gồ ghề
gỗ
gốc
gối
gội
gôm
gồm
gôn
gông
gồng
gộp vào
gột
gột rửa
gờ
gở
gỡ
gỡ rối
gởi
gởi gắm
gợi
gờm
gớm
gợn
gợt
gù
gù lưng
gục
gùi
guốc
guồng
gút
gừ
gửi
gửi gắm
gừng
gươm
gườm
gượm
gương
gương mẫu
gượng
gượng dậy
gượng nhẹ
ha
ha ha
hà
hà bá
hà hiếp
hà khắc
hà mã
hà tất
hà tiện
hả
hả giận
há
há hốc
hạ
hạ bộ
hạ cánh
hạ cấp
hạ chí
hạ cố
hạ du
hạ giá
hạ giọng
hạ lệnh
hạ lịnh
hạ mình
hạ thủy
hạc
hách
hạch
hạch nhân
hạch sách
hai
hai lòng
hai vợ chồng
hài
hài cốt
hài hòa
hài hước
hài kịch
hài lòng
hải
hải âu
hải cảng
hải cẩu
hải đảo
hải đăng
hải hà
hải lưu
hải lý
hải mả
hải ngoại
hải phận
hải quan
hải quân
hải tặc
hải vị
hải yến
hãi
hái
hại
ham
ham mê
ham muốn
hàm
hàm hồ
hàm số
hàm súc
hãm
hãm hại
hám
hạm
hạm đội
han
hàn
hàn gắn
hàn sĩ
hàn the
hàn thử biểu
hàn vi
hãn
hãn hữu
hán học
hạn
hạn chế
hạn hán
hạn hẹp
hang
hàng
hàng đầu
hàng giậu
hàng hải
hàng hóa
hàng không
hàng lậu
hàng loạt
hàng ngày
hàng ngũ
hàng rào
hàng tháng
hàng tuần
hàng xóm
hãng
háng
hạng
hạng người
hanh
hanh thông
hành
hành chánh
hành động
hành hạ
hành hình
hành khách
hành khất
hành lạc
hành lang
hành lý
hành pháp
hành quân
hành tây
hành trình
hành tung
hành văn
hành vi
hãnh diện
hãnh tiến
hạnh
hạnh kiểm
hạnh ngộ
hạnh phúc
hao
hao hụt
hao mòn
hao tổn
hào
hào hiệp
hào hoa
hào hùng
hào hứng
hào khí
hào kiệt
hào nhoáng
hào phóng
hào quang
hảo
hảo hán
hảo tâm
hão
háo
háo hức
hạo nhiên
hạp
hát
hát xiệc
hạt
hạt lệ
hạt tiêu
hàu
hay
hay lây
hãy
hãy còn
háy
hắc
hắc ín
hặc
hăm
hăm hở
hằm hằm
hằn
hằn học
hẳn
hắn
hăng
hăng hái
hằng
hằng hà sa số
hằng số
hắt
hắt hiu
hắt hơi
hắt hủi
hâm
hâm hấp
hâm mộ
hầm
hầm mỏ
hầm mộ
hầm trú ẩn
hẩm
hẩm hiu
hân hạnh
hân hoan
hận
hấp
hấp dẫn
hấp hối
hấp hơi
hấp tấp
hấp thụ
hất
hất hủi
hầu
hầu bao
hầu cận
hầu chuyện
hầu hạ
hầu hết
hẩu
hậu
hậu môn
hậu phương
hậu quả
hậu sản
hậu thế
hậu thuẫn
hậu tố
hậu trường
hậu vận
hẩy
he
hè
hé môi
hé mở
hé nắng
hé răng
hẹ
hèm
hẻm
hen
hèn
hèn hạ
hèn mạt
hèn mọn
hèn nhát
hèn yếu
hẹn
hẹn hò
heo
heo hút
heo nái
heo quay
hèo
hẻo lánh
héo
héo hắt
hẹp
hẹp lượng
hét
hề
hể hả
hễ
hệ
hệ quả
hệ thống
hệ trọng
hếch
hếch hoác
hếch mồm
hên
hến
hết
hết hồn
hết hơi
hết lòng
hết sức
hếu
hỉ nọ
hỉ nự
hí
hí hoáy
hí trường
hia
hích
hịch
hiềm nghi
hiềm oán
hiểm
hiểm ác
hiểm độc
hiểm họa
hiểm nghèo
hiếm
hiên
hiên ngang
hiền
hiền hòa
hiền sĩ
hiền triết
hiền từ
hiển hách
hiển nhiên
hiến
hiến chương
hiến pháp
hiện
hiện diện
hiện đại
hiện hành
hiện hình
hiện nay
hiện tại
hiện thân
hiện thực
hiện tình
hiện trạng
hiện tượng
hiện vật
hiếng
hiếp
hiếp dâm
hiệp
hiệp định
hiệp đồng
hiệp hội
hiệp thương
hiệp ước
hiểu
hiểu biết
hiểu lầm
hiếu
hiếu chiến
hiếu đễ
hiếu kỳ
hiếu thảo
hiệu
hiệu chính
hiệu đính
hiệu lệnh
hiệu lực
hiệu nghiệm
hiệu quả
hiệu số
hiệu suất
hiệu trưởng
hình dáng
hình dạng
hình dung
hình học
hình như
hình thể
hỉnh
híp
hít
hiu quạnh
ho
ho gà
ho hen
ho lao
hò
hò la
hò reo
họ
họ hàng
hoa
hoa hậu
hoa hiên
hoa hoét
hoa hồng
hoa kỳ
hoa lệ
hoa liễu
hoa lợi
hoa mỹ
hoa quả
hoa tiêu
hòa
hòa bình
hòa giải
hòa hợp
hòa khí
hòa nhã
hòa nhạc
hòa nhịp
hòa tan
hòa thuận
hỏa
hỏa châu
hỏa diệm sơn
hỏa hoạn
hỏa lực
hỏa pháo
hỏa táng
hỏa tiễn
hỏa xa
hóa
hóa chất
hóa đơn
hóa giá
hóa học
hóa thạch
hóa trang
họa
họa báo
họa đồ
họa mi
họa sĩ
hoạch định
hoài
hoài cổ
hoài nghi
hoài niệm
hoài vọng
hoại
hoại thư
hoan hỉ
hoan hô
hoan lạc
hoàn
hoàn cảnh
hoàn cầu
hoàn mỹ
hoàn tất
hoàn thành
hoàn thiện
hoàn toàn
hoàn vũ
hoãn
hoán chuyển
hoán dụ
hoán vị
hoạn
hoạn nạn
hoang
hoang dại
hoang dâm
hoang đường
hoang mang
hoang phế
hoang phí
hoang tàn
hoang vu
hoàng
hoàng cung
hoàng gia
hoàng hôn
hoàng oanh
hoàng thân
hoàng thượng
hoàng tộc
hoàng tử
hoảng
hoảng hốt
hoảng sợ
hoành hành
hoành tráng
hoạnh tài
hoạt bát
hoạt động
hoạt họa
hoắc
hoặc
hoắt
hóc
hóc búa
học
học bổng
học đường
học giả
học lực
học phí
học thuyết
học thức
học trò
học viên
học viện
học xá
hòe
hoi hóp
hỏi
hỏi cung
hỏi dò
hỏi han
hỏi tiền
hói
hòm
hòn
hòn bi
hòn dái
hong
hỏng
hóng mát
họng
hóp
họp
hót
hô
hô hấp
hồ
hồ đồ
hồ nghi
hồ sơ
hồ tắm
hổ
hổ phách
hổ thẹn
hỗ trợ
hố
hộ
hộ chiếu
hộ khẩu
hộ lý
hộ thân
hộ tịch
hộ tống
hộ vệ
hốc
hốc hác
hộc
hôi
hôi hám
hôi thối
hồi
hồi âm
hồi giáo
hồi hộp
hồi kí
hồi sinh
hồi tỉnh
hồi tưởng
hối
hối đoái
hối hận
hối lộ
hội
hội chẩn
hội chợ
hội chứng
hội đồng
hội nghị
hội ngộ
hội viên
hôm
hôm nay
hôn
hôn mê
hồn
hồn nhiên
hỗn độn
hỗn láo
hông
hồng
hồng hào
hồng nhan
hồng phúc
hồng tâm
hồng thập tự
hộp
hộp thư
hốt hoảng
hột
hơ
hờ
hở
hớ
hơi
hơi thở
hời
hơn
hơn thiệt
hờn dỗi
hờn giận
hớn hở
hớp
hợp
hợp âm
hợp chất
hợp đồng
hợp kim
hợp lí
hợp lực
hợp lưu
hợp pháp
hợp tác xã
hợp thức hóa
hớt
hủ tục
hũ
hú
hú hí
hụ
hùa
huân chương
huấn luyện
húc
huệ
hủi
hun
hun đúc
hùn
hung
hung ác
hung dữ
hung phạm
hung thần
hung tin
hung tợn
hùng biện
hùng cường
hùng tráng
hùng vĩ
húp
hụp
hút
hụt
huy chương
huy động
huy hiệu
huy hoàng
hủy
hủy bỏ
hủy diệt
hủy hoại
huyên náo
huyền
huyền bí
huyền diệu
huyễn
huyễn hoặc
huyện
huyết
huyết áp
huyết bạch
huyết cầu
huyết dụ
huyết quản
huyệt
huynh
huynh đệ
huỳnh quang
huýt
hư
hư danh
hư hại
hư không
hư thân
hư vô
hứa
hứa hẹn
hứa hôn
hưng phấn
hưng thịnh
hứng
hứng thú
hứng tình
hương
hương liệu
hương lửa
hương nhu
hương thơm
hương vị
hưởng
hưởng ứng
hướng
hướng dẫn
hướng thiện
hươu
hưu chiến
hưu trí
hữu
hữu cơ
hữu dụng
hữu hạn
hữu ích
hữu tình
hữu ý
hy hữu
hy sinh
hy vọng
hý họa
i tờ
ì
ì ạch
ị
ỉa
ích
ích kỷ
ích lợi
im
im lặng
im lìm
im phăng phắc
ỉm
in
in máy
inh ỏi
inh tai
ình
ít
ít có
ít hơn
ít khi
ít lâu nay
ít nhiều
ít nhứt
ít nói
ít nữa
ít ỏi
ỉu
ka ki
ka li
ke
kẻ
kẻ cắp
kẻ cướp
kẻ trộm
kẽ
kẽ hở
ké
kem
kèm
kẽm
kẽm gai
kém
kèn
kén
kẻng
keo
keo kiệt
kèo
kéo
kéo bè
kéo co
kéo cưa
kéo dài
kéo lê
kéo lưới
kẹo
kép
kép hát
kẹp
kẹp tóc
két
kẹt
kê
kê khai
kề
kể
kế
kế hoạch
kế thừa
kế tiếp
kế toán
kế tục
kế vị
kệ
kềm
kên kên
kênh
kềnh
kết án
kết duyên
kết giao
kết hôn
kết hợp
kết luận
kết nạp
kết quả
kết thúc
kêu
kêu gọi
kêu la
kêu nài
kêu oan
kêu vang
kha khá
khả ái
khả năng
khả nghi
khả ố
khả quan
khả thi
khá
khá giả
khá tốt
khác
khác gì
khác thường
khác xa
khạc
khách
khách hàng
khách khứa
khách quan
khách sạn
khách sáo
khai
khai báo
khai bút
khai hỏa
khai hóa
khai sanh
khai thác
khai trừ
khai trương
khai tử
khải hoàn
khải hoàn ca
khái niệm
khái quát
kham
kham khổ
khảm
khám
khám nghiệm
khám phá
khám xét
khan
khan hiếm
khán
khán đài
khán giả
khang trang
khảng khái
kháng
kháng án
kháng chiến
kháng sinh
khánh
khánh chúc
khánh kiệt
khánh thành
khánh tiết
khao
khao khát
khảo
khảo cổ
khảo cứu
khảo hạch
khảo sát
khạp
khát
khát máu
khát vọng
kháu
khay
khắc
khắc khoải
khắc khổ
khẳm
khắm
khăn
khằn
khăng
khăng khít
khẳng định
khắp
khắt khe
khấc
khâm liệm
khâm phục
khẩn cấp
khẩn trương
khấn
khất
khất nợ
khâu
khẩu
khẩu cái
khẩu cung
khẩu độ
khẩu hiệu
khẩu phần
khẩu trang
khẩu vị
khấu
khấu đầu
khấu hao
khấu trừ
khe
khe khắt
khẽ
khen
khen ngợi
khéo
khép
khét
khê
khế
khệnh khạng
khêu
khêu gợi
khều
khi
khi trước
khỉ
khí
khí cầu
khí chất
khí cốt
khí cụ
khí động học
khí giới
khí hậu
khí hậu học
khí lực
khí phách
khí quản
khí quyển
khí tượng
khía
khích động
khích lệ
khiêm nhường
khiếm diện
khiếm nhã
khiển trách
khiến
khiêng
khiếp
khiếp nhược
khiếp sợ
khiêu dâm
khiêu khích
khiêu vũ
khiếu
khiếu nại
khiếu tố
khinh
khinh bạc
khinh bỉ
khinh khí
khinh khí cầu
khinh thường
khít
kho
kho tàng
khó
khó chịu
khó coi
khó khăn
khó lòng
khó nghĩ
khó nhọc
khoa
khoa học
khoa trương
khỏa thân
khóa
khóa học
khóa luận
khóa tay
khoác
khoai
khoai nước
khoai sọ
khoai tây
khoái
khoái cảm
khoái lạc
khoan
khoan dung
khoan hồng
khoan thai
khoan thứ
khoản
khoản đãi
khoang
khoảng
khoảng khoát
khoáng chất
khoáng đạt
khoáng hóa
khoáng sản
khoáng vật học
khoanh
khoảnh khắc
khóc
khoe
khỏe mạnh
khóe
khoét
khỏi
khói
khom
khóm
khô
khô héo
khô mực
khổ
khổ dịch
khổ hạnh
khổ hình
khổ não
khổ sai
khổ sở
khổ tâm
khố
khốc liệt
khôi hài
khôi ngô
khôi phục
khối
khối lượng
khối óc
khôn
khôn khéo
khôn ngoan
khốn khổ
khốn nỗi
không
không bao giờ
không chiến
không chừng
không dám
không gian
không hề
không kể
không khí
không lực
không nhận
không phận
không quân
không sao
không thể
khổng giáo
khổng lồ
khống chế
khờ
khơi
khởi công
khởi hành
khởi xướng
khớp
khu giải phóng
khu trừ
khua
khuân
khuất phục
khuây khỏa
khuấy
khúc
khúc chiết
khúc khích
khúc khuỷu
khúc xạ
khuê các
khuếch đại
khuếch khoác
khuếch tán
khuếch trương
khui
khúm núm
khung
khùng
khủng bố
khủng hoảng
khủng khiếp
khuôn
khuôn khổ
khuôn mặt
khuôn mẫu
khuôn sáo
khuy
khuy bấm
khủy
khuya
khuyên
khuyên bảo
khuyên can
khuyên giải
khuyển
khuyến cáo
khuyến khích
khuyết
khuyết điểm
khuynh
khuynh đảo
khuynh hướng
khử trùng
khứ hồi
khứa
khước từ
khứu
kì
kì kèo
kí lô
kị sĩ
kia
kích
kích động
kích thích
kích thích tố
kích thước
kịch
kịch bản
kịch câm
kịch liệt
kiêm
kiềm
kiềm chế
kiềm tỏa
kiểm
kiểm duyệt
kiểm soát
kiếm
kiếm hiệp
kiên cố
kiên định
kiên gan
kiên nhẫn
kiên quyết
kiên trinh
kiến
kiến hiệu
kiến nghị
kiến thiết
kiến thức
kiến trúc
kiện
kiện tướng
kiêng
kiêng nể
kiếp
kiếp trước
kiết
kiệt quệ
kiệt sức
kiêu
kiêu căng
kiều dân
kiều diễm
kiểu
kiểu mẫu
kiệu
kim
kim anh
kim bằng
kim khí
kim loại
kim ngân
kim ô
kim tự tháp
kín
kín hơi
kinh
kinh dị
kinh doanh
kinh điển
kinh đô
kinh hoàng
kinh ngạc
kinh nghiệm
kinh nguyệt
kinh tế
kinh tế học
kinh thánh
kinh tuyến
kình
kính
kính chúc
kính hiển vi
kính phục
kính yêu
kíp
kíp nổ
kịp
kỳ
kỳ ảo
kỳ công
kỳ cục
kỳ cựu
kỳ dị
kỳ diệu
kỳ đà
kỳ giông
kỳ ngộ
kỳ quan
kỳ thi
kỳ thị
kỷ cương
kỷ luật
kỷ lục
kỷ nguyên
kỷ niệm
kỹ
kỹ nghệ
kỹ nữ
kỹ sư
kỹ thuật
kỹ viện
ký
ký giả
ký hiệu
ký họa
ký kết
ký ninh
ký sinh
ký sự
ký thác
ký túc xá
ký ức
kỵ
la
la bàn
la cà
la đà
la đơn
la hét
la liệt
la mắng
la ó
la tinh
là
là là
lả
lả lơi
lả tả
lá
lá bài
lá cải
lá chắn
lá cờ
lá lách
lá mía
lá sách
lá thăm
lạ
lạ đời
lạ kỳ
lạ lùng
lạ mặt
lạ thường
lác
lác đác
lạc
lạc đà
lạc đề
lạc điệu
lạc hậu
lạc loài
lạc lõng
lạc quan
lạc thú
lách
lách cách
lách tách
lạch
lạch bạch
lạch cạch
lạch đạch
lai
lai giống
lai lịch
lai rai
lai vãng
lài
lải
lải nhải
lãi
lái
lái buôn
lái đò
lái xe
lại
lại cái
lại sức
lam
lam chướng
lam lũ
lam nham
làm
làm ăn
làm bạn
làm bậy
làm biếng
làm cho
làm chủ
làm chứng
làm cỏ
làm công
làm dáng
làm dấu
làm dịu
làm dữ
làm đĩ
làm giả
làm giàu
làm hỏng
làm khoán
làm lại
làm lành
làm loạn
làm mẫu
làm nhục
làm phiền
làm quen
làm tiền
làm xong
lạm dụng
lạm phát
lan
lan can
lan tràn
làn
làn sóng
lang
lang bạt
lang băm
lang ben
lang thang
làng
lảng
lảng tránh
lảng vảng
lãng mạn
lãng phí
lãng quên
lãng tử
láng
láng giềng
lạng
lanh lẹ
lành
lành lặn
lãnh
lãnh chúa
lãnh đạm
lãnh đạo
lãnh địa
lãnh hải
lãnh hội
lãnh sự
lãnh thổ
lánh
lánh mặt
lánh nạn
lánh xa
lạnh
lạnh lẽo
lạnh lùng
lạnh người
lạnh nhạt
lao
lao công
lao đao
lao động
lao khổ
lao phiền
lao tâm
lao tù
lao xao
lảo đảo
lão
lão bà
lão bộc
lão giáo
lão luyện
lão suy
láo
láo nháo
lạp xưởng
lát
lát nữa
lạt
lau
lau chùi
làu
làu bàu
láu cá
láu lỉnh
lay
lay chuyển
lay động
lay ơn
lảy cò
láy
lạy
lắc
lắc lư
lăm le
lắm
lắm tiền
lăn
lăn lộn
lăn tay
lằn
lặn
lăng
lăng kính
lăng loàn
lăng mạ
lăng nhục
lăng quăng
lăng tẩm
lăng trụ
lăng xăng
lằng nhằng
lẳng lơ
lẵng
lắng
lắng tai
lặng
lặng lẽ
lặng ngắt
lắp
lắt nhắt
lặt vặt
lâm
lâm bệnh
lâm chung
lâm nạn
lâm thời
lầm
lầm bầm
lầm lạc
lầm lẫn
lầm lỗi
lầm lỳ
lầm than
lẩm bẩm
lẩm cẩm
lẫm liệt
lấm chấm
lấm lét
lấm tấm
lân
lân cận
lân quang
lân tinh
lần
lần hồi
lần lượt
lẩn
lẩn quẩn
lẩn quất
lẩn tránh
lẩn vào
lẫn
lẫn lộn
lấn
lận đận
lâng lâng
lấp
lấp lánh
lấp liếm
lấp ló
lập
lập chí
lập công
lập dị
lập kỷ lục
lập mưu
lập nghiệp
lập pháp
lập trường
lập tức
lật
lật đật
lật đổ
lật nhào
lật tẩy
lâu
lâu đài
lâu đời
lâu la
lầu
lầu xanh
lậu
lây
lây lất
lầy
lầy lội
lầy nhầy
lẫy lừng
lấy
lấy cớ
lấy cung
lấy lệ
lấy lòng
lấy xuống
le
le le
le lói
lè nhè
lẻ
lẻ loi
lẻ tẻ
lẽ
lẽ phải
lẽ ra
lẽ sống
lẽ thường tình
lé
lẹ
lem
lém
len
lèn
lén
lén lút
leng keng
leo
leo lẻo
leo lét
leo trèo
lèo tèo
lẻo
lẽo
lẽo đẽo
lẹo
lép
lép xẹp
lẹt đẹt
lê
lê thê
lề
lề đường
lề lối
lề mề
lề thói
lể
lễ
lễ bái
lễ độ
lễ giáo
lễ nghi
lễ nghĩa
lễ phép
lễ phục
lễ vật
lệ
lệ luật
lệ phí
lệ thuộc
lên
lên án
lên đường
lên giá
lên lớp
lên mặt
lên men
lênh đênh
lênh láng
lềnh bềnh
lệnh
lều
lếu láo
lì
lí lắc
lị
lìa
lịch
lịch lãm
lịch sử
lịch sự
liếc
liêm khiết
liêm sỉ
liếm
liệm
liên bang
liên bộ
liên can
liên doanh
liên đoàn
liên hệ
liên hiệp
liên hiệp quốc
liên hợp
liên khu
liên lạc
liên quan
liên tiếp
liên tỉnh
liên tưởng
liền
liền bên
liền tay
liễn
liến thoắng
liểng xiểng
liệng
liếp
liệt
liệt dương
liệt giường
liệt kê
liệt sĩ
liều
liều lĩnh
liều lượng
liễu
liệu
liệu pháp
lim
lim dim
lịm
linh
linh cảm
linh đình
linh hồn
linh thiêng
linh tinh
linh tính
lình
lính
lính quýnh
lịnh
líp
lít
lịu
lo
lo buồn
lo liệu
lo sợ
lò
lò hỏa táng
lò kò
lò xo
ló
lọ
lọ lem
loa
lòa
lõa lồ
lõa xõa
lóa
loạc choạc
loài
loại
loại bỏ
loại trừ
loan báo
loán
loạn
loạn dâm
loạn lạc
loạn luân
loạn thị
loạn trí
loang
loãng
loáng thoáng
loanh quanh
loạt
lóc
lọc
lọc lõi
lọc lừa
loe
loe loét
loe toe
lòe
lòe loẹt
lóe
loét
loi choi
loi ngoi
loi nhoi
lòi
lòi tói
lõi đời
lòm
lõm
lon
lọn
long
long lanh
long não
long trọng
lòng
lòng dân
lòng heo
lòng lang dạ thú
lòng nhân
lòng sông
lòng tốt
lỏng
lóng
lóng ngóng
lọng
lót
lót ổ
lọt
lọt lòng
lô
lô cốt
lỗ
lỗ đít
lỗ mãng
lỗ rún
lỗ tai
lố
lố lăng
lộ
lộ diện
lộ trình
lộc
lôi
lôi cuốn
lôi thôi
lồi
lỗi
lỗi thời
lối
lội
lốm đốm
lồn
lộn
lộn xộn
lông
lông mày
lông mi
lồng
lồng lộng
lộng lẫy
lộng quyền
lốp
lột
lột mặt nạ
lơ
lơ mơ
lờ
lờ đờ
lỡ
lời
lời hứa
lời khuyên
lời thề
lời tựa
lợi
lợi dụng
lợi tức
lởm chởm
lợm giọng
lờn
lớn
lợn
lớp
lớp lang
lợp
lợt
lu
lũ
lú
lùa
lúa
lúa mì
lúa thóc
lụa
luân chuyển
luân lạc
luân lý
luẩn quẩn
luận án
luận đề
luận điệu
luận văn
luật
luật gia
luật học
luật khoa
luật lao động
luật sư
lúc
lúc lắc
lục
lục địa
lục đục
lục vấn
lui
lủi
lủi thủi
lùn
lún
lụn bại
lung lạc
lung lay
lủng
lủng củng
lũng đoạn
lúng túng
luộc
luôn
luồn
luồn cúi
luồng
luồng điện
luồng tư tưởng
luống cuống
lụp xụp
lụt
lũy
lũy tiến
luyến ái
luyện
luyện thi
lữ điếm
lữ khách
lừa
lừa đảo
lửa
lứa
lựa
lực
lực lưỡng
lực lượng
lực sĩ
lưng
lừng lẫy
lửng lơ
lược
lược đồ
lược khảo
lược thuật
lười biếng
lưỡi
lưỡi gươm
lưỡi khoan
lưỡi lê
lưới
lưới nhện
lưới tình
lườm
lượm
lươn
lươn lẹo
lượn
lương
lương khô
lương tâm
lương thiện
lương thực
lưỡng lự
lưỡng quyền
lượng
lượng thứ
lướt
lượt
lưu
lưu danh
lưu đày
lưu động
lưu hành
lưu lạc
lưu luyến
lưu manh
lưu tâm
lưu thông
lưu vong
lưu vực
lựu
lựu đạn
ly
ly biệt
ly bôi
ly dị
ly hương
ly tán
ly tâm
lý
lý do
lý giải
lý hóa
lý lịch
lý luận
lý thuyết
lý trí
lý tưởng
ma
ma cà bông
ma cà rồng
ma cô
ma dút
ma két
ma lem
ma lực
ma men
ma quỷ
ma túy
mà
mà cả
mả
mã
mã hóa
mã lực
mã não
mã phu
mã tấu
mã thượng
má
má đào
mạ
mạ bạc
mạ điện
mạ vàng
mác
mạc
mách
mạch
mạch lạc
mạch máu
mạch nha
mai
mai hoa
mai mái
mai mối
mai phục
mai sau
mai táng
mài
mài miệt
mải
mãi dâm
mãi mãi
mái
mái chèo
mái hiên
mái tóc
man
man di
man mác
man rợ
man trá
màn
màn ảnh
màn bạc
mãn
mãn nguyện
mạn
mang
mang máng
mang tiếng
màng
màng nhĩ
màng trinh
mảng
mãng cầu
mãng xà
máng
mạng
mạng bạc
mạng lưới
mạng mỡ
mạng nhện
manh
manh mối
manh nha
manh tâm
mành
mảnh mai
mãnh liệt
mãnh thú
mánh lới
mạnh
mạnh dạn
mạnh khỏe
mao quản
mào
mạo hiểm
mạo nhận
mát
mạt
mạt cưa
mạt sát
mạt vận
mau
mau chóng
mau mắn
màu
màu mè
màu mỡ
màu sắc
máu
máu tham
may
may mà
may mắn
may sẵn
mày
máy
máy chữ
máy giặt
máy in
máy tính
mắc
mắc cỡ
mắc lừa
mắc nợ
mặc
mặc cảm
mặc dầu
mặc dù
mặc niệm
mặc sức
mắm
mặn
mặn nồng
măng
măng cụt
măng đô
măng tây
mắng
mắt
mắt cá
mắt lưới
mặt
mặt hàng
mặt nạ
mặt phẳng
mặt tiền
mặt trăng
mặt trận
mâm
mầm
mầm non
mân mê
mẫn cán
mận
mấp máy
mấp mé
mấp mô
mập
mập mạp
mập mờ
mất
mất cắp
mất dạy
mất mùa
mất ngủ
mất tích
mất trí
mật
mật độ
mật khu
mật lệnh
mật mã
mật mía
mật ong
mật vụ
mâu thuẫn
mẫu
mẫu đơn
mẫu giáo
mẫu hệ
mẫu mã
mẫu số
mấu
mậu dịch
mây
me
mè
mẻ
mé
mẹ
men
men sứ
men tình
meo
mèo
méo
mẹo
mép
mét
mê
mê lộ
mê ly
mê man
mê mê
mê muội
mê sảng
mê tín
mềm
mềm mỏng
mền
mến
mến phục
mênh mông
mệt
mệt mỏi
mếu
mì
mí mắt
mị dân
mỉa mai
mía
miên man
miền
miễn
miễn cưỡng
miễn dịch
miễn phí
miễn thuế
miễn thứ
miễn trừ
miếng
miệng
miệng lưỡi
miệt mài
miêu tả
miếu
mỉm cười
mím
mìn
minh bạch
minh châu
minh họa
minh mẫn
mình
mistake
mít
mò
mỏ
mỏ neo
mỏ vàng
mỏ vịt
mõ
móc
móc sắt
mọc
mọc răng
moi
mọi
mõm
mòn
món
mong
mong manh
mỏng
mỏng tanh
móng tay
móng vuốt
mót
mọt
mô
mô hình
mô phạm
mô phỏng
mô tả
mô tô
mô tơ
mồ
mồ côi
mồ hôi
mổ
mổ xẻ
mộ bia
mộ chí
mộ địa
mộ phần
mộc mạc
môi
môi giới
mồi
mỗi
mối
mối tình
môn
môn bài
môn đệ
môn học
môn phái
mông
mông quạnh
mộng
mộng du
mộng mị
mốt
một
một chút
một vài
mơ
mơ hồ
mơ mộng
mơ tưởng
mơ ước
mờ
mở
mở đầu
mở màn
mở mang
mở mắt
mở miệng
mỡ
mớ
mời
mới
mơn trớn
mu
mù
mù mịt
mủ
mũ
mua
mua bán
mua chuộc
mua sắm
mua vui
mùa
mùa màng
múa
múa võ
mục đích
mục đồng
mục kích
mục kỉnh
mục lục
mục tiêu
mui
mùi
mùi soa
mùi vị
mũi
mũi tên
muỗi
muối
muốn
muộn
mưa
mửa
mực
mừng
mướn
mượn
mưu
mưu sinh
mỹ lệ
mỹ nữ
mỹ thuật
mỹ vị
mỹ ý
na
na ná
na pan
na tri
nả
nã
ná
ná cao su
nạc
nách
nách lá
nai
nai lưng
nài
nài nỉ
nải
nái
nam
nam châm
nam cực
nam nữ
nam tính
nám
nạm
nan
nan giải
nản
nạn
nạn nhân
nang
nàng
nàng dâu
nàng hầu
nàng tiên
nạng
nanh
nanh ác
nanh sấu
nanh vuốt
nao lòng
nao núng
nào
não
não nùng
náo nhiệt
nạo
nạo óc
nạo vét
nạp
nạp thuế
nát
nát nhàu
nát óc
nạt nộ
nay
này
nảy
nảy ra
nạy
năm
năm học
năm mươi
nằm
nằm mê
nằm ngủ
nằm vạ
nắm
nắm xương
nắn
năng lực
năng lượng
năng nổ
năng suất
nắng
nắng ráo
nặng
nặng lời
nặng mùi
nặng nề
nặng nhọc
nặng tình
nắp
nấc
nấm
nâng
nâng đỡ
nấp
nâu
nấu ăn
nẻ
né
né tránh
needly
nem
ném
nén
nén giận
nén lòng
neo
nẻo
nép
nẹp
nét
nề hà
nể
nêm
nếm
nệm
nên
nền
nền móng
nền nếp
nền tảng
nêu
nếu
nếu không
nga
nga văn
ngà
ngà ngà say
ngà voi
ngả
ngả lưng
ngả mũ
ngả nghiêng
ngã
ngã nước
ngạc nhiên
ngách
ngai
ngài
ngái ngủ
ngại
ngại ngùng
ngàn
ngán
ngạn
ngạn ngữ
ngang
ngang hàng
ngang ngửa
ngang nhiên
ngang trái
ngáng
ngành ngọn
ngảnh cổ
ngạnh
ngao
ngào
ngào ngạt
ngáo
ngạo
ngạo mạn
ngạo nghễ
ngáp
ngạt
ngạt hơi
ngạt ngào
ngay
ngay cả
ngay đơ
ngay khi
ngay thẳng
ngay thật
ngày
ngày công
ngày giỗ
ngày giờ
ngày lễ
ngày mai
ngày mùa
ngày nay
ngày ngày
ngày sinh
ngày tháng
ngày xưa
ngáy
ngắm
ngăn
ngăn cấm
ngăn nắp
ngắn
ngắt
ngặt nghèo
ngâm
ngâm nga
ngầm
ngẫm
ngấm
ngậm
ngậm ngùi
ngân
ngân hà
ngân hàng
ngân khoản
ngân phiếu
ngân quỹ
ngân sách
ngần ngại
ngần ngừ
ngẩn ngơ
ngập
ngập ngừng
ngất ngưởng
ngẫu hứng
ngẫu nhiên
ngây dại
ngây ngất
ngây thơ
nghe
nghe lén
nghẹn
nghẹn ngào
nghèo
nghèo hèn
nghèo nàn
nghèo túng
nghẹt mũi
nghề
nghệ
nghệ nhân
nghệ sĩ
nghệ thuật
nghển
nghênh chiến
nghênh tân
nghi
nghi thức
nghi vấn
nghỉ
nghỉ việc
nghĩ
nghị định
nghị hòa
nghị luận
nghị lực
nghị quyết
nghị sĩ
nghĩa
nghĩa địa
nghĩa vụ
nghịch
nghịch cảnh
nghiêm
nghiêm cấm
nghiêm khắc
nghiêm trọng
nghiên cứu
nghiền
nghiến
nghinh
nghinh chiến
nghinh ngang
ngỏ
ngõ
ngõ hẻm
ngó
ngoài
ngoài đường
ngoài ra
ngoại giao
ngoại ngữ
ngoại ô
ngoại quốc
ngoại thương
ngoạm
ngoan
ngoan cố
ngoan ngoãn
ngoạn mục
ngoằn ngèo
ngọc
ngọc lan
ngọc trai
ngòi
ngòi viết
ngói
ngon
ngón chân
ngọn
ngọn ngành
ngọt
ngô
ngộ độc
ngộ nhận
ngốc
ngôi
ngồi
ngồi ì
ngồi tù
ngôn ngữ
ngôn từ
ngông cuồng
ngỗng
ngơ ngác
ngờ
ngỡ
ngu
ngu dân
ngủ
ngũ
ngũ quan
ngũ vị
ngụ
ngụ ngôn
ngục
nguội
nguồn
nguồn gốc
nguy hiểm
nguy nga
ngụy trang
nguyên chất
nguyên nhân
nguyên tắc
nguyên tử
nguyện vọng
nguyệt cầm
ngư phủ
ngữ pháp
ngứa
ngựa
ngựa cái
ngựa ô
ngực
ngừng
ngược đãi
người
người đẹp
người điên
người ta
người yêu
ngưỡng mộ
ngượng
ngượng nghịu
ngưu
nha
nha khoa
nha phiến
nha sĩ
nhà
nhà ăn
nhà bác học
nhà báo
nhà bè
nhà bếp
nhà chứa
nhà ga
nhà hàng
nhà in
nhà khách
nhà lãnh đạo
nhà máy
nhà nghề
nhà nước
nhà riêng
nhà tang
nhà táng
nhà tắm
nhà thơ
nhà thờ
nhà thương
nhà trọ
nhà văn
nhà xuất bản
nhã nhặn
nhá nhem
nhạc
nhai
nhài
nhái
nhàm
nhám
nhan sắc
nhàn
nhàn du
nhàn nhã
nhãn
nhãn cầu
nhãn hiệu
nhãn khoa
nhãn lực
nhạn
nhang
nhanh
nhanh chóng
nhanh nhẹn
nhanh trí
nhánh
nhạo
nhát
nhạt
nhau
nhàu
nhay
nhảy
nhảy dù
nhảy sào
nhảy vọt
nhảy xa
nháy
nhắc
nhắc lại
nhắc nhở
nhằm
nhắm
nhắm hướng
nhăn
nhăn mặt
nhăn nheo
nhăn nhíu
nhăn nhó
nhẵn nhụi
nhặng
nhắp
nhặt
nhân
nhân ái
nhân bản
nhân cách
nhân chứng
nhân công
nhân danh
nhân dân
nhân dịp
nhân đạo
nhân đức
nhân hậu
nhân khẩu
nhân loại
nhân tạo
nhân từ
nhân viên
nhẫn
nhẫn nại
nhẫn tâm
nhấn mạnh
nhận
nhận biết
nhận chìm
nhận định
nhận lời
nhận mặt
nhận ra
nhận thức
nhập khẩu
nhập ngũ
nhất
nhất định
nhất quán
nhất quyết
nhất trí
nhật báo
nhật ký
nhật thực
nhậu
nhẹ
nhẹ dạ
nheo nhóc
nhện
nhi đồng
nhi khoa
nhì
nhì nhằng
nhì nhèo
nhĩ
nhí
nhí nhảnh
nhị
nhị trùng âm
nhiễm bịnh
nhiễm sắc
nhiệm kỳ
nhiệm mầu
nhiệm vụ
nhiên liệu
nhiếp ảnh
nhiệt độ
nhiệt liệt
nhiệt lượng
nhiều
nhiều lời
nhiều tiền
nhiễu nhương
nhìn
nhìn nhận
nhìn thấy
nhịn đói
nhịn nhục
nhỉnh
nhíp
nhịp
nho
nho gia
nho giáo
nho học
nho nhã
nho nhỏ
nho sĩ
nhỏ
nhỏ nhặt
nhỏ nhẻ
nhỏ nhẹ
nhỏ nhen
nhọc nhằn
nhóm
nhón gót
nhọn
nhổ cỏ
nhổ răng
nhồi bột
nhồi sọ
nhôm
nhộn
nhộn nhịp
nhông
nhồng
nhộng
nhốt
nhột
nhơ
nhơ nhuốc
nhờ
nhớ
nhớ nhà
nhớt
nhu cầu
nhu động
nhu mì
nhu nhược
nhũ dịch
nhũ tương
nhuận trường
nhục
nhục dục
nhục đậu khấu
nhục hình
nhục mạ
nhục nhã
nhục thể
nhuệ khí
nhún nhường
nhung
nhúng
nhuộm
như
như thế
như vầy
như vậy
nhử
nhựa
nhựa sống
nhức
nhức răng
nhưng
nhược điểm
nhường lại
nhường nhịn
nhượng bộ
ni cô
ni lông
ni tơ
nỉ
nia
nĩa
ních
niêm
niêm luật
niêm phong
niêm yết
niềm nở
niên
niên đại
niên giám
niêu thiếu
nín
nín khóc
nịnh hót
níu
no
nỏ
nó
nọc
nói
nói bậy
nói chuyện
nói dối
nói đùa
nói giùm
nói lái
nói láo
nói lắp
nói lên
nói liều
nói lóng
nói năng
nói quanh
nói thật
non nước
nón
nóng
nóng lòng
nô đùa
nô lệ
nổ
nổ súng
nồi
nổi
nổi giận
nổi tiếng
nối
nối nghiệp
nội bộ
nội các
nội chiến
nội chính
nội công
nội dung
nội địa
nội động từ
nội gián
nội hóa
nội khóa
nội thương
nội tiết
nội trợ
nội trú
nội vụ
nôm
nông
nông cạn
nông dân
nông sản
nồng hậu
nồng nàn
nốt
nơ
nở
nỡ to
nợ
nơi
nới
nơm
nụ
nụ cười
nùi
núi
núi lửa
núi non
núm
núm vú
nung
nung nấu
nũng nịu
nuôi
nuôi dưỡng
nuôi nấng
nuôi tầm
nuông chiều
nuốt
nuốt chửng
nuốt giận
núp
nút
nữ
nữ công
nữ giới
nữ hoàng
nữ sinh
nữ tính
nữ trang
nửa
nửa đêm
nửa tá
nữa
nựng
nước
nước da
nước đá
nước hoa
nước uống
nương
nương náu
nướng
nứt
nứt ra
o
o bế
ó
oa oa
oa trữ
òa
oác oác
oách
oai
oai danh
oai hùng
oai linh
oai nghiêm
oai oái
oai vệ
oải
oái ăm
oan
oan cừu
oan hồn
oan nghiệt
oan trái
oan uổng
oán
oán ghét
oán giận
oán hận
oán than
oán trách
oanh kích
oanh liệt
oằn
oắt
oắt con
óc
óc châm biếm
ọc
ọc ạch
oi
oi ả
oi bức
oi khói
oi nồng
oi nước
ói
ói máu
om
om sòm
òm ọp
ong
ong mật
ong nghệ
ong thợ
ong vò vẽ
ỏng bụng
ỏng ẹo
óng ả
óng ánh
ót
ô
ô chữ
ô danh
ô hay
ô hô
ô hợp
ô nhiễm
ô nhục
ô tô
ô trọc
ô uế
ồ
ồ ạt
ổ
ổ bi
ổ chuột
ổ gà
ổ khóa
ổ kiến
ổ mối
ốc
ốc xà cừ
ôi
ổi
ối
ôm
ôm ấp
ôm chân
ôm đồm
ồm ộp
ốm
ốm yếu
ôn
ôn đới
ôn hòa
ôn tập
ôn tồn
ồn
ổn
ổn định
ông
ông bà
ông tổ
ông tướng
ông vãi
ống
ống chân
ống chỉ
ống điếu
ống khói
ống nhòm
ống tiêm
ống trời
ốp
ốt dột
ơ
ở
ở đời
ở riêng
ở trọ
ớ
ợ
ới
ỡm ờ
ơn
ớn
ớn lạnh
ớt
pha
pha lê
pha trò
phà
phá
phá án
phá bĩnh
phá đám
phá giá
phá hại
phá hoại
phá hủy
phá kỷ lục
phá phách
phá quấy
phá rối
phá sản
phá thai
phá trinh
phác
phác họa
phách
phách lối
phai
phải
phải biết
phải cách
phải chăng
phải đạo
phải lẽ
phải lòng
phải quấy
phái
phái bộ
phái đẹp
phái đoàn
phái viên
phàm
phàm phu
phàm tục
phạm
phạm nhân
phạm pháp
phạm trù
phạm vi
phàn nàn
phản
phản ánh
phản chiếu
phản công
phản dân chủ
phản đề
phản đối
phản động
phản nghịch
phản ứng
phản xạ
phán
phán quyết
phang
phảng phất
phanh
phanh phui
phanh thây
phao
phao tin
pháo
pháo binh
pháo bông
pháo đài
pháo kích
pháp
pháp chế
pháp lí
pháp lịnh
pháp luật
phát
phát biểu
phát đạt
phát giác
phát hành
phát minh
phát ngôn
phát thanh
phát xít
phạt
phẳng
phẳng lặng
phẳng lì
phẳng phiu
phẩm
phẩm chất
phẩm giá
phẩm hạnh
phẩm vật
phân
phân biệt
phân bón
phân cấp
phân chất
phân chia
phân công
phân giải
phân loại
phân ly
phân số
phân tích
phân tử
phân ưu
phần
phần thưởng
phấn
phấn chấn
phấn đấu
phấn hoa
phấn khởi
phấn nộ
phận sự
phất
phất phơ
phật
phật tử
phe
phe cánh
phe đảng
phe phái
phè phỡn
phen
phèn
phèng la
phép
phép lạ
phép tính
phê bình
phê chuẩn
phế bỏ
phế nhân
phế phẩm
phế tật
phế truất
phế vật
phệ
phễu
phi
phi cảng
phi công
phi cơ
phi đội
phi hành đoàn
phi lý
phi thường
phì nhiêu
phỉ báng
phí phạm
phí tổn
phía
phía trước
phích nước
phịch
phiếm du
phiếm luận
phiếm thần
phiên
phiên âm
phiên dịch
phiền
phiền hà
phiền lòng
phiền muộn
phiền nhiễu
phiền phức
phiến
phiến loạn
phiện
phiêu lưu
phiếu
phiếu xuất
phim
phím
phỉnh gạt
pho tượng
phò
phò mã
phó
phó bản
phó mát
phó thác
phó từ
phong
phong bì
phong cảnh
phong dao
phong kiến
phong lan
phong nhã
phong phú
phong tỏa
phong trào
phòng
phòng ăn
phòng bệnh
phòng bị
phòng dịch
phòng đợi
phòng không
phòng ngự
phòng ngừa
phòng thí nghiệm
phòng xa
phỏng
phỏng đoán
phỏng tác
phỏng vấn
phóng
phóng đãng
phóng thích
phóng uế
phóng viên
phóng xạ
phô trương
phổ biến
phổ thông
phố
phôi pha
phôi thai
phổi
phồng
phơi
phơi bày
phơi phới
phu
phu mỏ
phu nhân
phu thê
phù du
phù hợp
phù phép
phù phiếm
phù rễ
phù sa
phù thủy
phủ
phủ đầu
phủ định
phủ nhận
phủ quyết
phũ
phũ phàng
phú nông
phú quí
phú thương
phụ
phụ âm
phụ bạc
phụ cấp
phụ dịch
phụ huynh
phụ khoa
phụ lái
phụ lục
phụ nữ
phụ tá
phụ thân
phụ trách
phụ trương
phụ tùng
phúc
phúc đức
phúc trình
phục
phục dịch
phục kích
phục sinh
phục viên
phun
phung phí
phụng
phụng dưỡng
phụng sự
phút
phức tạp
phương
phương châm
phương diện
phương pháp
phương thuốc
phương thức
phương tiện
phương trình
phường
phượng
pin
qua
qua đời
qua loa
qua lọc
qua ngày
qua quít
quà
quà cáp
quà sáng
quà tặng
quả
quả cảm
quả cân
quả cật
quả đấm
quả đất
quả quyết
quả tang
quá
quá cố
quá độ
quá khứ
quá trình
quạ
quai hàm
quái dị
quái vật
quan điểm
quan hệ
quan niệm
quan sát
quan tài
quan trọng
quản
quản đốc
quản gia
quản lý
quản ngại
quản thúc
quản trị
quán
quán quân
quán tính
quán trọ
quán xuyến
quang
quang cảnh
quang đãng
quang học
quang minh
quang phổ
quang tuyến
quang vinh
quàng
quàng xiên
quảng cáo
quảng đại
quảng trường
quãng
quáng
quáng gà
quanh
quanh co
quanh quẩn
quanh quất
quành
quánh
quạnh hiu
quạnh quẽ
quào
quát
quát mắng
quạt
quay
quay cóp
quay cuồng
quay đơ
quay phim
quay quắt
quảy
quắc
quắc thước
quắm
quặm
quăn
quăn queo
quằn
quằn quại
quắn
quặn
quăng
quặng
quắp
quặp
quắt
quắt quéo
quặt
quặt quẹo
quân
quân bị
quân bình
quân ca
quân cảng
quân cảnh
quân chính
quân chủ
quân công
quân dịch
quân địch
quân đoàn
quân đội
quân hàm
quân hiệu
quân khu
quân kỳ
quân lệnh
quân lính
quân luật
quân lực
quân nhân
quân pháp
quân phiệt
quân quản
quân sĩ
quân số
quân sư
quân sự
quân tử
quân y
quần
quần áo
quần chúng
quần đảo
quần thần
quần tụ
quần vợt
quẩn
quẫn bách
quẫn trí
quấn
quấn quít
quận
quận chúa
quận công
quận trưởng
quận vương
quầng
quất
quất hồng bì
quật
quật cường
quật khởi
quây
quây quần
quầy
quấy
quấy nhiễu
quấy rầy
quấy rối
quậy
que
que đan
que hàn
què
què quặt
quẻ
quen
quen biết
quen thói
quèn
queo
quéo
quẹo
quét
quét dọn
quét tước
quẹt
quê
quê hương
quê mùa
quê người
quế
quên
quên lãng
quết
quết trần
quệt
qui
qui chế
qui định
qui mô
qui trình
qui ước
quì
quỉ
quỉ quyệt
quỉ thuật
quĩ
quĩ đạo
quĩ tích
quí
quí khách
quí phái
quí tộc
quí vật
quị
quít
quịt
quốc
quốc ca
quốc công
quốc dân
quốc doanh
quốc gia
quốc giáo
quốc hội
quốc huy
quốc hữu hóa
quốc khánh
quốc kỳ
quốc lộ
quốc ngữ
quốc phòng
quốc tế
quốc tịch
quốc văn
quốc xã
quơ
quở
quở trách
quyên
quyên sinh
quyền
quyền bính
quyền hạn
quyền hành
quyền lợi
quyền lực
quyền thuật
quyền uy
quyển
quyến luyến
quyến rũ
quyến thuộc
quyết
quyết chiến
quyết định
quyết liệt
quyết tâm
quyết toán
quỳnh
quỳnh tương
ra
ra dáng
ra đi
ra đời
ra hiệu
ra lịnh
ra mắt
ra mặt
ra oai
ra rả
ra rìa
ra sức
ra tòa
ra vẻ
rá
rạ
rác
rạc
rạc cẳng
rách
rách rưới
rạch
rạch ròi
rải
rải rác
rải rắc
rái cá
ram
rám nắng
rạm
rán
rạn
rạn nứt
rang
ràng
ràng buộc
rạng rỡ
ranh
ranh con
ranh giới
ranh ma
ranh mãnh
rành
rành mạch
rảnh
rảnh mắt
rảnh rang
rảnh tay
rãnh
rao
rào
ráo
ráo riết
rạo rực
ráp
rạp
rạp hát
rát
rau
rày
ráy tai
rắc
rắc rối
rắn
rắn chắc
rắn dọc dưa
rắn hổ lửa
rắn hổ mang
rắn lục
răng
răng cửa
răng giả
răng khôn
răng nanh
rằng
rặng
râm
râm bụt
rầm rì
rầm rộ
rậm
rần rần
rận
rập
rập rờn
rất
rất mực
râu
rầu
rây
rầy
rầy rà
rẫy
rè
rẻ
rẽ
rèm
ren
rèn
rèn luyện
reo
réo
rét
rê
rể
rễ
rế
rên
rên xiết
rệp
rết
rêu
rêu rao
rì rào
rỉ
ria
rìa
rỉa
riêng
riêu cua
rịn
ring
rình
rịt
rìu
rỏ
rõ
rõ ràng
rọ
róc
róc rách
rọc
roi
roi da
rọi
rón rén
rong
rong chơi
rong huyết
ròng
ròng rọc
rót
rô
rồ
rổ
rỗ
rồi
rỗi
rối
rối loạn
rối ren
rối rít
rối trí
rốn
rồng
rỗng
rống
rộng
rộng lớn
rộng lượng
rộng thênh thang
rốt cuộc
rơ
rờ
rợ
rơi
rơi lệ
rơi rớt
rời
rời rã
rời rạc
rơm
rơm rác
rớt
ru
ru ngủ
rủ rê
rũ
rũ rượi
rú
rùa
rủa
rũa
rúc
rục
rục rịch
rủi
run
run sợ
rung
rung động
rùng mình
rùng rợn
rụng
rụng rời
ruốc
ruồi
ruồng bỏ
ruồng rẫy
ruộng
ruộng đất
ruộng muối
ruộng nương
ruột
ruột gà
ruột già
ruột non
ruột thừa
rút
rút lui
rút ngắn
rụt
rụt rè
rửa
rửa ảnh
rửa nhục
rửa tội
rữa
rựa
rực rỡ
rưng rưng
rừng
rừng rậm
rước
rước khách
rưỡi
rưới
rườm rà
rướm
rương
rường cột
rượt
rượt theo
rượu
rượu bia
rượu chát
rượu đế
rượu vang
sa
sa bàn
sa chân
sa cơ
sa đà
sa đề
sa đọa
sa lầy
sa mạc
sa ngã
sa sầm
sa sẩy
sa sút
sa thải
sà
sà lan
sà lúp
sả
sá
sá bao
sá chi
sá gì
sá kể
sạ
sách
sách giáo khoa
sách lược
sách nhiễu
sách trắng
sách vở
sạch
sạch bong
sạch mắt
sạch sẽ
sạch trơn
sạch trụi
sai
sai bảo
sai biệt
sai lạc
sai lầm
sai ngoa
sai sót
sai số
sai trái
sài lang
sải
sải cánh
sái
sam
sàm báng
sàm nịnh
sám hối
sạm
san bằng
san định
san hô
san sát
san sẻ
sàn
sàn sàn
sản
sản hậu
sản khoa
sản lượng
sản nghiệp
sản phẩm
sản sinh
sản vật
sản xuất
sán
sán dây
sán lá
sán lãi
sán xơ mít
sạn
sang
sang ngang
sang sảng
sang số
sang tay
sang tên
sang trọng
sàng
sàng lọc
sảng
sảng khoái
sáng
sáng bóng
sáng chế
sáng choang
sáng chói
sáng dạ
sáng kiến
sáng lập
sáng loáng
sáng mắt
sáng ngời
sáng rực
sáng sớm
sáng sủa
sáng suốt
sáng tác
sáng tai
sáng tạo
sáng trưng
sáng ý
sanh
sành
sành sỏi
sánh
sánh bước
sánh duyên
sánh vai
sao
sao bản
sao băng
sao chép
sao cho
sao chổi
sao đành
sao hôm
sao mai
sao tẩm
sao tua
sào
sào huyệt
sào sạo
sáo
sáo sậu
sạo
sap
sáp
sáp nhập
sat
sát
sát cánh
sát hạch
sát hại
sát khí
sát nhân
sát sạt
sát sinh
sát trùng
sạt nghiệp
sau
sau đó
sau hết
sau lưng
sau này
sau rốt
sáu
sáu mươi
say
say đắm
say mê
say sưa
sắc
sắc bén
sắc cạnh
sắc chỉ
sắc chiếu
sắc đẹp
sắc lệnh
sắc mặt
sắc sảo
sắc thái
sặc
sặc sỡ
sặc sụa
săm
săm lốp
sắm
sắm sửa
sắm vai
sặm màu
săn
săn bắn
săn bắt
săn sóc
sẵn
sẵn có
sẵn dịp
sẵn lòng
sẵn sàng
sắn
sắn dây
săng
sằng sặc
sắp
sắp chữ
sắp đặt
sắp hàng
sắp xếp
sắt
sắt son
sắt tây
sâm
sâm banh
sâm cầm
sầm
sầm uất
sẩm tối
sẫm
sấm
sấm ngôn
sấm sét
sậm sựt
sân
sân bay
sân bóng
sân cỏ
sân khấu
sân si
sân vận động
sần
sần sùi
sẩn
sấn
sấn sổ
sấp
sấp mặt
sấp ngửa
sập
sâu
sâu cay
sâu độc
sâu kín
sâu mọt
sâu róm
sâu sắc
sầu
sầu khổ
sầu muộn
sầu thảm
sấu
sây sát
sầy
sẩy
sẩy chân
sẩy tay
sẩy thai
sấy
sậy
se
sẻ
sẽ
sẽ hay
séc
sém
sen
sẹo
sét
sề
sệ
sệ nệ
sên
sểnh
sểnh tay
sệt
sếu
si
si tình
sì
sỉ
sỉ nhục
sĩ diện
sĩ phu
sĩ quan
sĩ số
sĩ tốt
sĩ tử
sịch
siểm nịnh
siêng
siêng năng
siết
siêu
siêu âm
siêu cường
siêu đẳng
siêu nhân
siêu nhiên
siêu phàm
siêu thanh
siêu tự nhiên
sinh
sinh dục
sinh dưỡng
sinh đôi
sinh động
sinh hạ
sinh hóa học
sinh hoạt
sinh học
sinh kế
sinh khí
sinh lực
sinh lý
sinh lý học
sinh mệnh
sinh nhật
sinh quán
sinh ra
sinh sản
sinh sắc
sinh sống
sinh sự
sinh thái học
sinh thời
sinh tố
sinh tồn
sinh trưởng
sinh tử
sinh vật
sinh vật học
sinh viên
sình
sình lầy
sính
sít
sít sao
so
so bì
so le
so sánh
sò
sọ
sọ dừa
soán đoạt
soạn
soạn giả
soạn thảo
soát
sóc
sọc
soi
soi xét
sỏi
sõi
sói
sóm sém
sọm
son
son sắt
son trẻ
song
song hành
song hỉ
song le
song mã
song phương
song song
song thân
song toàn
sòng
sòng bạc
sòng phẳng
sóng
sóng gió
sóng sánh
sóng sượt
soóc
sót
sọt
sô cô la
sô vanh
sồ
sổ
sổ lông
sổ lồng
sổ sách
sổ tay
sỗ sàng
số
số bị chia
số chia
số đông
số hạng
số học
số liệu
số lượng
số một
số tử vi
sôi
sôi gan
sôi nổi
sôi sục
sồi
sồn sồn
sồn sột
sông
sông ngòi
sông núi
sổng
sống
sống chết
sống còn
sống sít
sống sót
sống sượng
sống thừa
sống trâu
sộp
sốt
sốt dẻo
sốt rét
sốt ruột
sốt sắng
sốt vó
sột soạt
sơ
sơ bộ
sơ cấp
sơ đồ
sơ giao
sơ hở
sơ khai
sơ khảo
sơ lược
sơ mi
sơ qua
sơ sinh
sơ suất
sơ tán
sơ thẩm
sơ ý
sờ
sờ mó
sờ sờ
sở
sở cầu
sở đoản
sở hữu
sở khanh
sở nguyện
sở tại
sở thích
sở thú
sở trường
sớ
sợ
sợ hãi
sởi
sợi
sớm
sớm hôm
sớm mai
sớm tối
sơn
sơn ca
sơn cốc
sơn dầu
sơn dương
sơn hào
sơn khê
sơn mài
sơn nhân
sơn thần
sơn thủy
sờn
sờn lòng
sởn
sởn mởn
sớt
stand.
stick
su hào
su su
sú
sụ
sủa
suất
súc
súc sắc
súc sinh
súc tích
súc vật
sục
sục sạo
sui
sùi
sùi sụt
sủi bọt
sum họp
sum sê
sum vầy
sụm
sún
sụn
sung
sung công
sung huyết
sung mãn
sung sức
sung sướng
sung túc
sùng
sùng bái
sùng đạo
sùng kính
sủng ái
súng
súng cao su
súng cối
súng lục
súng ngắn
súng trường
suối
suối vàng
suôn
suôn sẻ
suông
suồng sã
suốt
suốt đời
súp de
sụp
sụp đổ
sút
sút kém to
sụt
suy
suy biến
suy di
suy diễn
suy đồi
suy luận
suy lý
suy nghĩ
suy nhược
suy rộng ra
suy suyển
suy tàn
suy thoái
suy tôn
suy xét
suy yếu
suyễn
suýt
suýt nữa
suýt soát
sư
sư cụ
sư đệ
sư huynh
sư phạm
sư phó
sư phụ
sư trưởng
sư tử
sử
sử dụng
sử gia
sử học
sử ký
sử lược
sử sách
sứ
sứ đoàn
sứ giả
sứ mệnh
sứ quán
sự
sự cố
sự kiện
sự nghiệp
sự thể
sự thế
sự thực
sự tích
sự vật
sự việc
sửa
sửa chữa
sửa đổi
sửa sang
sửa soạn
sữa
sứa
sức
sức ép
sức khỏe
sức lực
sức mạnh
sức nặng
sức sống
sức vóc
sực nức
sưng
sưng húp
sừng
sừng sỏ
sừng sững
sửng
sửng cồ
sửng sốt
sững
sững sờ
sưởi
sưởi nắng
sườn
sương
sương giá
sương mù
sướng
sướng mắt
sượng
sượng mặt
sướt
sứt
sứt môi
sưu tầm
sưu tập
sưu thuế
ta
ta thán
tà
tà dâm
tà dương
tà khí
tà ma
tà tâm
tà thuật
tà thuyết
tà vẹt
tả
tả chân
tả đạo
tả khuynh
tả ngạn
tả thực
tả tơi
tã
tá
tá dược
tá điền
tá lý
tá tràng
tạ
tạ thế
tác dụng
tác động
tác giả
tác hại
tác loạn
tác nhân
tác phẩm
tác phong
tác phúc
tác quái
tác thành
tạc
tạc dạ
tạc đạn
tách
tách bạch
tạch
tai
tai ác
tai ách
tai biến
tai hại
tai họa
tai nạn
tai quái
tai tiếng
tai ương
tài
tài cán
tài chính
tài công
tài đức
tài giảm
tài giỏi
tài hoa
tài khóa
tài khoản
tài liệu
tài lực
tài mạo
tài năng
tài nghệ
tài nguyên
tài phiệt
tài sản
tài sắc
tài tình
tài trí
tài tử
tài vụ
tài xế
tài xỉu
tải
tãi
tái
tái bản
tái bút
tái cử
tái diễn
tái giá
tái hồi
tái hợp
tái ngũ
tái phạm
tái phát
tái sản xuất
tái sinh
tái tạo
tái thế
tại
tại chỗ
tại chức
tại đào
tại gia
tại ngũ
tại sao
tại tâm
tại vì
tam
tam bản
tam cấp
tam đại
tam điểm
tam đoạn luận
tam giác
tam giáo
tam suất
tam thất
tam thể
tam tòng
tam tộc
tám
tám mươi
tạm
tạm bợ
tạm thời
tạm trú
tạm ứng
tạm ước
tan
tan hoang
tan nát
tan rã
tan tác
tan tành
tan vỡ
tàn
tàn ác
tàn bạo
tàn binh
tàn dư
tàn hại
tàn hương
tàn khốc
tàn lụi
tàn nhang
tàn nhẫn
tàn phá
tàn phế
tàn sát
tàn tạ
tàn tật
tàn tệ
tàn tích
tản bộ
tản cư
tản mạn
tản mát
tản văn
tán
tán loạn
tán thành
tán thưởng
tán tỉnh
tán tụng
tang
tang chế
tang chứng
tang lễ
tang phục
tang thương
tang tích
tang tóc
tang vật
tàng hình
tàng tàng
tàng trữ
tảng
tảng lờ
tảng sáng
tạng
tạng phủ
tanh
tanh bành
tanh hôi
tánh
tạnh
tạnh ráo
tao
tao đàn
tao ngộ
tao nhã
tào lao
tảo
tảo ngộ
tảo thanh
táo
táo bạo
táo gan
táo tác
tạo
tạo giao
tạo hình
tạo hóa
tạo lập
tạo thành
táp
tạp
tạp chất
tạp chí
tạp kỹ
tạp lục
tạp nhạp
tạp vụ
tát
tạt
tạt tai
tàu
tàu chiến
tàu chợ
tàu cuốc
tàu hỏa
tàu ngầm
tàu sân bay
tàu thủy
tay
tay áo
tay lái
tay nải
tay ngang
tay quay
tay sai
tay thợ
tay trắng
tay trên
tay trong
tay vịn
tày
tày đình
tày trời
táy máy
tắc
tắc kè
tắc nghẽn
tắc trách
tắc xi
tăm
tăm hơi
tăm tích
tằm
tắm
tắm giặt
tắm nắng
tắm rửa
tằn tiện
tăng
tăng cường
tăng lữ
tăng ni
tằng tịu
tằng tổ
tằng tôn
tặng
tặng phẩm
tặng thưởng
tắt
tắt hơi
tắt kinh
tắt thở
tấc
tấc lòng
tâm
tâm can
tâm đắc
tâm địa
tâm giao
tâm hồn
tâm linh
tâm lý
tâm lý học
tâm não
tâm nhĩ
tâm phúc
tâm sự
tâm thành
tâm thần
tâm thất
tâm tình
tâm tính
tâm trạng
tâm trí
tâm tư
tầm
tầm bậy
tầm gửi
tầm nã
tầm phào
tầm tã
tầm thường
tầm vóc
tầm vông
tầm xích
tầm xuân
tẩm
tẩm bổ
tẩm quất
tấm
tấm bé
tân binh
tân hôn
tân khách
tân kỳ
tân lang
tân ngữ
tân thời
tân tiến
tân trào
tân xuân
tần ngần
tần số
tần tảo
tẩn mẩn
tấn
tấn công
tấn phong
tận
tận cùng
tận dụng
tận hiểu
tận hưởng
tận lực
tận tâm
tận thế
tận tình
tận tụy
tâng bốc
tầng
tầng lớp
tấp nập
tập
tập đoàn
tập hậu
tập hợp
tập huấn
tập kết
tập kích
tập luyện
tập quán
tập san
tập sự
tập tành
tập thể
tập trung
tập tục
tất
tất cả
tất nhiên
tất tả
tất yếu
tật
tật bệnh
tẩu
tẩu mã
tẩu tán
tẩu thoát
tấu
tậu
tây
tây bắc
tây cung
tây học
tây nam
tây phương
tẩy
tẩy chay
tẩy não
tẩy trừ
tấy
te
tè
tẻ
tẽ
té
té ra
tem
tem phiếu
tem tép
tém
ten
teng beng
teo
tẹo
tép
tét
tẹt
tê
tê bại
tê giác
tê mê
tê tê
tê thấp
tề tựu
tễ
tế
tế bào
tế bào chất
tế độ
tế nhị
tế thế
tệ
tệ bạc
tệ đoan
tệ hại
tệ tục
tệ xá
tếch
têm
tên
tên gọi
tên hiệu
tên lửa
tên thánh
tên tục
tênh
tết
tếu
tha
tha hóa
tha hồ
tha ma
tha thứ
thà
thả
thả cửa
thả dù
thả lỏng
thả rong
thác
thạc sĩ
thách
thách thức
thạch
thạch anh
thạch bản
thạch cao
thạch lựu
thạch nhũ
thạch sùng
thạch tùng
thai
thai nghén
thải
thải hồi
thái
thái ấp
thái bình
thái cực
thái dương
thái độ
thái giám
thái hậu
thái quá
thái thượng hoàng
thái tử
thái y
tham
tham chiến
tham chính
tham gia
tham khảo
tham luận
tham mưu
tham nhũng
tham quan
tham sinh
tham tài
tham tàn
tham thiền
tham vọng
thảm
thảm cảnh
thảm hại
thảm họa
thảm khốc
thảm sát
thảm thiết
thảm thương
thám
thám hiểm
thám thính
thám tử
than
than bùn
than cám
than chì
than củi
than ôi
than phiền
than xỉ
thản nhiên
thán phục
thán từ
thang
thang máy
thảng hoặc
tháng
tháng ngày
tháng tháng
thanh
thanh bạch
thanh bình
thanh cảnh
thanh danh
thanh đạm
thanh giáo
thanh kiếm
thanh la
thanh lịch
thanh liêm
thanh minh
thanh nhàn
thanh nữ
thanh quản
thanh tao
thanh tâm
thanh thản
thanh thiên
thanh thoát
thanh tịnh
thanh toán
thanh tra
thanh trừng
thanh vắng
thanh vân
thành
thành công
thành danh
thành đạt
thành hình
thành hôn
thành kiến
thành kính
thành lũy
thành ngữ
thành niên
thành phẩm
thành phần
thành phố
thành quả
thành sự
thành tâm
thành thạo
thành thân
thành thị
thành thử
thành tích
thành tựu
thành văn
thành viên
thành ý
thảnh thơi
thánh
thánh ca
thánh chỉ
thánh cung
thánh đản
thánh địa
thánh đường
thánh giá
thánh nhân
thánh sư
thánh thi
thánh thượng
thạnh
thao
thao diễn
thao láo
thao luyện
thao lược
thao tác
thao trường
thao túng
thảo
thảo luận
thảo mộc
thảo nguyên
tháo
tháo dạ
tháo lui
tháo vát
thạo
tháp
tháp canh
tháp ngà
thạp
thau
tháu
thay
thay chân
thay đổi
thay mặt
thay phiên
thay vì
thảy
thắc mắc
thắc thỏm
thăm
thăm dò
thăm viếng
thẳm
thắm
thằn lằn
thăng
thăng bằng
thăng hoa
thăng thiên
thăng tiến
thăng trầm
thằng bờm
thằng cha
thẳng
thẳng cánh
thẳng đứng
thẳng giấc
thẳng góc
thẳng tay
thẳng thắn
thẳng thừng
thắng
thắng cảnh
thắng lợi
thắng thế
thắng trận
thặng dư
thắp
thắt
thắt chặt
thắt cổ
thắt lưng
thâm
thâm ảo
thâm cung
thâm độc
thâm giao
thâm hiểm
thâm kín
thâm nhập
thâm niên
thâm tâm
thâm thùng
thâm tình
thâm trầm
thâm ý
thầm
thầm lặng
thẩm
thẩm định
thẩm mỹ
thẩm mỹ học
thẩm phán
thẩm quyền
thẩm vấn
thẫm
thấm
thấm nhuần
thấm thía
thấm thoát
thậm chí
thân
thân ái
thân cận
thân danh
thân hành
thân hình
thân hữu
thân mật
thân mến
thân phận
thân thể
thân thế
thân thiện
thân thiết
thân thuộc
thần
thần bí
thần chú
thần diệu
thần đồng
thần học
thần hồn
thần kinh
thần kỳ
thần linh
thần lực
thần phục
thần quyền
thần sạ
thần sắc
thần thánh
thần thoại
thần thông
thần tình
thần tốc
thần tượng
thẩn thơ
thận
thận trọng
thấp
thấp hèn
thấp thoáng
thập ác
thập cẩm
thập kỷ
thập phân
thập phương
thập toàn
thập tự
thất bại
thất bát
thất cách
thất chí
thất đức
thất hiếu
thất học
thất kinh
thất lạc
thất lễ
thất nghiệp
thất nhân tâm
thất phu
thất sách
thất sắc
thất sủng
thất thân
thất thế
thất thố
thất thủ
thất thường
thất tiết
thất tín
thất tình
thất trận
thất truyền
thất ước
thất vận
thất vọng
thất ý
thật
thật thà
thầu
thầu dầu
thầu khoán
thấu
thấu đáo
thấu kính
thây
thây ma
thầy
thầy bói
thầy chùa
thầy dòng
thầy giáo
thầy ký
thầy phán
thầy pháp
thầy thuốc
thầy tu
thầy tướng
thấy
the
the thé
thè
thè lè
thẻ
thẻ bài
thèm
thèm khát
thèm muốn
then
then chốt
thẹn
thẹn mặt
thẹn thùng
theo
theo dõi
theo đuổi
theo gương
thèo lẻo
thẹo
thép
thẹp
thét
thê
thê lương
thê thảm
thề
thề bồi
thề nguyền
thể
thể cách
thể chất
thể chế
thể diện
thể dục
thể hiện
thể lệ
thể lực
thể nghiệm
thể tất
thể thao
thể theo
thể thống
thể tích
thế
thế cục
thế gian
thế giới
thế giới quan
thế hệ
thế kỷ
thế lực
thế nào
thế phẩm
thế sự
thế thái
thế thì
thế tộc
thế tục
thế ước
thế vận hội
thêm
thêm bớt
thềm
thênh thang
thếp
thết
thêu
thêu thùa
thều thào
thi
thi công
thi cử
thi đua
thi hành
thi hào
thi hứng
thi nhân
thi pháp
thi sĩ
thi thể
thi thố
thi tứ
thi vị
thì
thì giờ
thì phải
thì thào
thì thầm
thì thọt
thí
thí dụ
thí điểm
thí mạng
thí nghiệm
thí sinh
thị
thị chính
thị dân
thị giác
thị hiếu
thị lực
thị sảnh
thị thực
thị tộc
thị trấn
thị trường
thị trưởng
thị xã
thìa
thích
thích đáng
thích hợp
thích khách
thích nghi
thích thú
thích ứng
thích ý
thiếc
thiên
thiên can
thiên chúa
thiên chúa giáo
thiên cổ
thiên đỉnh
thiên định
thiên đô
thiên đường
thiên hạ
thiên hướng
thiên kiến
thiên lôi
thiên mệnh
thiên nga
thiên nhiên
thiên sứ
thiên tai
thiên tài
thiên tạo
thiên thần
thiên thể
thiên thời
thiên tính
thiên tuế
thiên tử
thiên văn học
thiên vị
thiền
thiền gia
thiền môn
thiển
thiển ý
thiến
thiện
thiện cảm
thiện chí
thiện chiến
thiện nghệ
thiện tâm
thiện xạ
thiện ý
thiêng liêng
thiếp
thiệp
thiết
thiết bì
thiết giáp
thiết kế
thiết lập
thiết mộc
thiết tha
thiết thân
thiết thực
thiết yếu
thiệt
thiệt hại
thiệt mạng
thiêu
thiêu hủy
thiêu thân
thiều quang
thiểu não
thiểu số
thiếu
thiếu hụt
thiếu máu
thiếu nhi
thiếu phụ
thiếu sinh quân
thiếu sót
thiếu tá
thiếu tướng
thiếu úy
thím
thinh
thình
thình lình
thỉnh
thỉnh cầu
thỉnh giáo
thỉnh nguyện
thỉnh thị
thỉnh thoảng
thính
thính giả
thính giác
thịnh
thịnh đạt
thịnh hành
thịnh nộ
thịnh soạn
thịnh thế
thịnh tình
thịnh trị
thịnh vượng
thíp
thịt
thiu
thiu thối
thò
thò lò
thỏ
thỏ thẻ
thọ
thoa
thỏa
thỏa chí
thỏa đáng
thỏa hiệp
thỏa lòng
thỏa mãn
thỏa thích
thỏa thuận
thóa mạ
thoai thoải
thoải mái
thoái hóa
thoái thác
thoảng
thoáng qua
thoát nợ
thoát thân
thoạt tiên
thoăn thoắt
thóc gạo
thọc
thoi
thỏi
thói
thói quen
thói tục
thon
thong dong
thòng
thọt
thô
thô bỉ
thô sơ
thô tục
thổ
thổ dân
thổ lộ
thổ nhưỡng
thổ phỉ
thổ tinh
thôi
thôi miên
thôi thúc
thổi
thổi phồng
thối
thối nát
thôn
thôn dã
thôn nữ
thôn quê
thôn tính
thồn
thổn thức
thông
thông báo
thông cảm
thông cáo
thông dụng
thông điệp
thông đồng
thông lệ
thông minh
thông qua
thông số
thông tấn xã
thông thạo
thông thường
thông tin
thông tục
thống chế
thống đốc
thống khổ
thống lĩnh
thống nhất
thống trị
thộp
thốt
thốt nốt
thơ
thơ ấu
thờ
thờ ơ
thở
thở dài
thớ
thợ
thợ bạc
thợ cạo
thợ cưa
thợ điện
thợ đúc
thợ hàn
thợ lặn
thợ may
thợ máy
thợ mộc
thợ rèn
thợ sơn
thời bình
thời cơ
thời đại
thời gian
thời khóa biểu
thời kỳ
thời sự
thời tiết
thời trang
thời vụ
thơm
thơm tho
thu
thu dọn
thu gom
thu hoạch
thu hồi
thu hút
thu lượm
thu nhập
thu thanh
thu xếp
thù địch
thù lao
thù oán
thủ bút
thủ công
thủ đô
thủ lĩnh
thủ phạm
thủ quân
thủ quỹ
thủ thuật
thủ thư
thủ tiêu
thủ trưởng
thủ tục
thủ tướng
thú
thú nhận
thú vị
thú vui
thụ động
thụ phấn
thụ thai
thụ tinh
thua
thua thiệt
thuần
thuần hóa
thuần khiết
thuần lý
thuần nhất
thuần phát
thuần phong mỹ tục
thuần thục
thuần túy
thuận
thuận tiện
thuật
thuật ngữ
thúc bách
thúc dục
thúc ép
thúc thủ
thuê
thuế
thuế thân
thui thủi
thụi
thủm
thun
thung lũng
thùng
thùng thư
thủng
thúng
thúng mủng
thuốc
thuốc bắc
thuốc bổ
thuốc cao
thuốc dán
thuốc độc
thuốc lá
thuốc lào
thuốc mê
thuốc muối
thuốc nam
thuốc ngủ
thuốc nhuộm
thuốc phiện
thuốc tẩy
thuộc
thuộc địa
thuộc tính
thuổng
thuở
thút thít
thụt
thụt lùi
thùy mị
thủy chung
thủy điện
thủy động lực học
thủy ngân
thủy sư đô đốc
thủy thủ
thủy tinh
thủy tổ
thủy triều
thuyên chuyển
thuyền
thuyền chài
thuyền thúng
thuyền trưởng
thuyết
thuyết giáo
thuyết phục
thuyết trình
thư
thư ký
thư lại
thư phòng
thư sinh
thư thả
thư thái
thư tín
thư từ
thư viện
thử
thử thách
thứ
thứ bậc
thứ trưởng
thứ tự
thứ yếu
thưa
thưa kiện
thưa thớt
thừa
thừa hành
thừa hưởng
thừa kế
thừa nhận
thừa số
thừa thãi
thức
thức dậy
thức tỉnh
thực
thực chất
thực dân
thực dụng
thực đơn
thực hành
thực hiện
thực nghiệm
thực quyền
thực ra
thực sự
thực tại
thực tập
thực tế
thực thể
thực trạng
thực từ
thực vật học
thừng
thước
thước dây
thước kẻ
thược dược
thương
thương cảm
thương gia
thương hại
thương lượng
thương mại
thương nhớ
thương số
thương tâm
thương tích
thương tổn
thương vụ
thường
thường khi
thường ngày
thường nhật
thường niên
thường thường
thường trực
thường xuyên
thưởng
thưởng thức
thượng cấp
thượng đẳng
thượng đế
thượng đỉnh
thượng hạng
thượng khách
thượng nghị viện
thượng phẩm
thượng sách
thượng sĩ
thượng tầng
thượng tầng kiến trúc
thượng tọa
thượng tướng
thượng uyển
thượng võ
ti hí
ti tiện
ti toe
tì
tì mẩn
tì vết
tỉ mỉ
tỉ tê
tí chút
tí hon
tí nữa
tí tách
tí teo
tí ti
tí tị
tí xíu
tị nạn
tia
tỉa
tía
tía tô
tích
tích cực
tích phân
tích trữ
tịch liêu
tịch thu
tiếc
tiếc rẻ
tiệc
tiệc rượu
tiệc trà
tiêm
tiềm lực
tiềm tàng
tiềm thức
tiếm
tiệm
tiệm ăn
tiên
tiên cảnh
tiên đề
tiên đoán
tiên nga
tiên nữ
tiên phong
tiên quyết
tiên tiến
tiên tri
tiền
tiền bạc
tiền cọc
tiền của
tiền đề
tiền định
tiền đồ
tiền lẻ
tiền mặt
tiền nhân
tiền phong
tiền sử
tiền tệ
tiền tiêu
tiền trạm
tiền tuyến
tiễn
tiễn biệt
tiến
tiến bộ
tiến độ
tiến hành
tiến sĩ
tiến thoái
tiến tới
tiến trình
tiện
tiện nghi
tiện tay
tiếng
tiếng động
tiếng lóng
tiếng nói
tiếng tăm
tiếng vang
tiếp
tiếp cận
tiếp chuyện
tiếp đãi
tiếp đón
tiếp giáp
tiếp kiến
tiếp nhận
tiếp nối
tiếp quản
tiếp tân
tiếp theo
tiếp thu
tiếp tục
tiếp viện
tiết
tiết diện
tiết kiệm
tiết lộ
tiết mục
tiệt trùng
tiêu
tiêu biểu
tiêu chuẩn
tiêu cực
tiêu diệt
tiêu dùng
tiêu đề
tiêu điểm
tiêu điều
tiêu độc
tiêu hao
tiêu hóa
tiêu tan
tiêu thụ
tiêu vong
tiêu xài
tiều tụy
tiểu ban
tiểu bang
tiểu đoàn
tiểu đội
tiểu học
tiểu luận
tiểu nhân
tiểu quy mô
tiểu sử
tiểu thuyết
tiểu thừa
tiểu tiện
tiểu trừ
tiểu tư sản
tiểu xảo
tiếu lâm
tim
tìm
tìm hiểu
tím
tin
tin cậy
tin đồn
tin vịt
tín dụng
tín hiệu
tín nhiệm
tín phiếu
tinh bột
tinh cầu
tinh chất
tinh chế
tinh dầu
tinh dịch
tinh giản
tinh hoa
tinh hoàn
tinh khiết
tinh nhuệ
tinh tế
tinh thần
tinh tú
tinh vi
tình
tình cảm
tình cờ
tình hình
tình nguyện
tình nhân
tình thật
tình thế
tình tiết
tình trạng
tình ý
tình yêu
tỉnh
tỉnh dậy
tỉnh lỵ
tỉnh táo
tĩnh dưỡng
tĩnh học
tĩnh tại
tĩnh tọa
tính
tính cách
tính chất
tính khí
tính nết
tính toán
tính từ
tít
tít mù
tịt
to
to béo
to lớn
to patch
to tát
to tướng
tò mò
tò vò
tỏ
tỏ ra
tỏ tường
tỏ vẻ
tòa án
tòa nhà
tòa soạn
tỏa
tọa đàm
tọa độ
tọa hưởng
tọa lạc
tọa thiền
toạc
toan
toan tính
toàn
toàn bộ
toàn diện
toàn lực
toàn phần
toàn quốc
toàn quyền
toàn thể
toán
toán học
toang hoác
tóc
tóc mai
tóc tơ
tóe
toét
toi
toi mạng
tỏi
tỏi tây
tom góp
tõm
tóm
tóm lại
tóm tắt
tòn tèn
tòng phạm
tòng quân
tọng
tóp tép
tọt
tô
tô điểm
tô vẽ
tổ
tổ chức
tổ hợp
tổ quốc
tổ tiên
tố cáo
tố giác
tố khổ
tố tụng
tốc
tốc độ
tốc hành
tốc ký
tộc
tôi
tôi tớ
tồi
tồi tệ
tối
tối cao
tối đa
tối hậu thư
tối mịt
tối nghĩa
tối tân
tối thiểu
tội
tội ác
tội phạm
tội vạ
tôm
tôm he
tôm hùm
tôn
tôn chỉ
tôn giáo
tôn nghiêm
tôn sùng
tôn ti
tôn trọng
tồn kho
tồn tại
tổn hại
tổn thất
tổn thương
tốn
tốn kém
tông tích
tổng bí thư
tổng cộng
tổng đài
tổng hành dinh
tổng hội
tổng hợp
tổng kết
tổng quát
tổng số
tổng tham mưu
tổng tuyển cử
tống biệt
tống cổ
tống giam
tống ngục
tốp
tốt
tốt bụng
tốt lành
tốt mã
tốt nghiệp
tốt số
tốt tiếng
tột đỉnh
tột độ
tơ
tơ hồng
tơ tưởng
tờ
tớ
tơi bời
tới
tới lui
tợn
tợp
tra
tra cứu
tra khảo
trà
trả
trả đũa
trả hàng
trả lời
trả thù
trác táng
trác tuyệt
trạc
trách
trách mắng
trách nhiệm
trai
trai trẻ
trải
trải qua
trái
trái khoáy
trái mùa
trái nghĩa
trái phép
trái xoan
trại
tràm
trảm
trám
trạm
tràn
tràn trề
trán
trang
trang bị
trang điểm
trang hoàng
trang nghiêm
trang sức
trang trí
trang trọng
tràng giang đại hải
tráng
tráng lệ
tráng miệng
trạng thái
tranh
tranh cãi
tranh cử
tranh đua
tranh luận
tranh thủ
tránh
tránh tiếng
trao
trao đổi
trao tay
trào
trào lưu
trào phúng
tráo trở
tráp
trát
trau chuốt
trau dồi
trắc
trắc bá diệp
trắc địa học
trắc nghiệm
trặc
trăm
trăn
trăn trở
trằn trọc
trăng
trăng gió
trắng
trắng bạch
trắng dã
trắng đục
trắng ngà
trắng ngần
trắng tay
trắng toát
trắng trợn
trâm
trầm
trầm hương
trầm mặc
trầm trọng
trân
trân châu
trân trọng
trần
trần gian
trần tình
trần trụi
trần truồng
trấn an
trấn áp
trấn giữ
trấn tĩnh
trận
trận địa
trận tuyến
trâng tráo
trập trùng
trật
trật tự
trâu
trâu bò
trâu nước
trầu
trấu
trầy
tre
trẻ
trẻ con
trẻ trung
trẻ tuổi
treo
treo giải
trèo
trèo trẹo
tréo ngoe
trẹo
trẹo hàm
trét
trể
trễ
trễ nải
trên
trệt
trêu
trêu ngươi
trêu tức
tri ân
tri giác
tri kỷ
tri thức
trì dộn
trì hoãn
trí
trí khôn
trí lực
trí nhớ
trí óc
trí thức
trí tuệ
trị
trị giá
trị sự
trị tội
trị vì
trích
trích dẫn
trịch thượng
triền miên
triển lãm
triển vọng
triện
triết gia
triết học
triệt để
triệt hạ
triệt tiêu
triều đại
triều đình
triều nghi
triều thần
triệu
triệu phú
triệu tập
trinh bạch
trinh nữ
trinh tiết
trình
trình báo
trình diễn
trình diện
trình độ
trình tự
trịnh trọng
trìu mến
tro
trò
trò chơi
trò chuyện
trò đùa
trò hề
trò vui
trỏ
tróc
trọc
trói
trói buộc
tròm trèm
tròn
tròn trịa
tròn vo
trọn
trong
trong khi
trong sạch
trong sáng
trong suốt
trong vòng
tròng trành
trọng
trọng âm
trọng đại
trọng điểm
trọng lưc
trọng lượng
trọng tài
trọng tải
trọng thưởng
trọng yếu
trót lọt
trổ
trôi
trôi chảy
trôi giạt
trồi
trỗi dậy
trội
trộm
trộm nghĩ
trốn
trộn
trông
trông cậy
trông chờ
trông coi
trông ngóng
trồng
trống
trống canh
trống không
trống trải
trơ
trơ tráo
trơ trọi
trơ trụi
trở
trở giọng
trở gót
trở lại
trở mặt
trở nên
trở ngại
trở về
trở xuống
trớ trêu
trợ cấp
trợ động từ
trợ lý
trợ thủ
trời
trời ơi
trơn
trơn tru
trớn
trợn
trớt
trợt
tru tréo
trù bị
trù chân
trù tính
trù trừ
trú ẩn
trú ngụ
trụ
truân chuyên
truất phế
trúc đào
trục
trục trặc
trục xuất
trùm
trung
trung bình
trung cấp
trung du
trung đoàn
trung đội
trung gian
trung hòa
trung khu
trung lập
trung niên
trung sĩ
trung tá
trung tâm
trung thành
trung thu
trung thực
trung tuần
trung ương
trung văn
trùng dương
trùng hợp
trùng lập
trùng tu
trũng
trúng
trúng cử
trúng số
trúng tủ
trúng tuyển
truông
trút
truy đuổi
truy kích
truy nã
truy nguyên
truy tố
trụy lạc
truyền
truyền bá
truyền cảm
truyền hình
truyền thanh
truyền thống
truyền thụ
truyền thuyết
truyện
truyện ký
trừ
trừ diệt
trừ khử
trừ phi
trữ
trữ tình
trứ danh
trưa
trực
trực giác
trực giao
trực khuẩn
trực quan
trực thăng
trực tiếp
trực tràng
trưng bày
trưng dụng
trưng thu
trừng
trừng phạt
trừng trị
trứng
trứng cá
trứng nước
trước
trước đây
trước khi
trước mặt
trước nhất
trước tiên
trườn
trương
trường
trường ca
trường đua
trường học
trường hợp
trường kỷ
trường phái
trường thọ
trưởng
trưởng ga
trưởng khoa
trưởng phòng
trưởng thành
trượt
trượt tuyết
trừu tượng
tu
tu dưỡng
tu hú
tu huýt
tu mi
tu sửa
tu thân
tu từ
tu viện
tù
tù binh
tù hãm
tù túng
tù và
tủ chè
tủ kính
tủ lạnh
tủ sách
tụ điện
tụ họp
tua
túa
tuân lệnh
tuân thủ
tuần báo
tuần dương hạm
tuần hành
tuần lễ
tuần tra
tuấn kiệt
tuấn tú
túc cầu
túc hạ
túc trực
tục
tục huyền
tục lệ
tục ngữ
tục tằn
tục tĩu
tủi thân
túi
túi tham
tum húp
tùm
tũm
túm
tụm
tun hút
tủn mủn
tung
tung tích
tung tóe
tùng bách
tùng tiệm
túng quẫn
túng thế
tụng niệm
tuổi
tuổi thọ
tuổi thơ
tuổi trẻ
tuôn
tuồng như
tuốt
tuột
tuy
tuy nhiên
tuy rằng
tuy thế
tùy
tùy bút
tùy thân
tùy theo
tùy thích
tùy tùng
tùy viên
tủy
tụy
tuyên bố
tuyên dương
tuyên ngôn
tuyên truyền
tuyền đài
tuyển
tuyển dụng
tuyển mộ
tuyến
tuyết
tuyệt
tuyệt chủng
tuyệt diệu
tuyệt đối
tuyệt luân
tuyệt tác
tuyệt tích
tuyệt vọng
tuyệt vời
tư
tư bản
tư cách
tư chất
tư duy
tư hữu
tư lệnh
tư liệu
tư lợi
tư pháp
tư sản
tư thế
tư thù
tư thục
tư tưởng
tư vấn
từ
từ bi
từ biệt
từ bỏ
từ chối
từ điển
từ điển học
từ nguyên
từ nối
từ pháp
từ thiện
từ thông
từ tính
từ tốn
từ vựng
từ vựng học
tử cung
tử lộ
tử ngữ
tử sĩ
tử tế
tử thần
tử trận
tử vi
tứ chi
tứ đức
tứ giác
tứ khoái
tứ phía
tứ quý
tứ tuần
tứ tung
tự cao
tự cấp
tự chủ
tự do
tự đắc
tự động
tự động hóa
tự giác
tự hào
tự học
tự lập
tự lực
tự nguyện
tự nhiên
tự phát
tự phong
tự quyết
tự sát
tự thú
tự tiện
tự tin
tự trị
tự trọng
tự túc
tự xưng
tự ý
tựa
tựa hồ
tức cười
tức giận
tức là
tức thì
tức tốc
tưng bừng
từng
từng trải
tước
tước đoạt
tươi
tươi cười
tươi tắn
tưới
tươm tất
tương đắc
tương đối
tương đương
tương lai
tương quan
tương trợ
tương tư
tương ứng
tường
tường tận
tường thuật
tưởng
tưởng nhớ
tưởng tượng
tướng
tướng mạo
tượng
tượng hình
tượng trưng
tửu điếm
tửu sắc
ty
tỳ
tỷ
tỷ giá
tỷ lệ
tỷ số
tỷ trọng
u
u ám
u ẩn
u hồn
u ơ
u ran
u sầu
u tịch
u uất
ù
ủ
ủ dột
ủ ê
ủ rũ
ú ớ
ú ụ
ùa
ủa
úa
uẩn khúc
uất hận
uất ức
ục ịch
uể oải
uế khí
ủi
úi
úi chà
um tùm
ùm
ung
ung dung
ung nhọt
ung thư
ủng
ủng hộ
úng
uốn
uốn nắn
uốn quanh
uống
úp
úp mở
út
ụt ịt
uy danh
uy hiếp
uy lực
uy nghi
uy phong
uy quyền
uy thế
uy tín
ủy ban
ủy mị
ủy quyền
ủy thác
ủy viên
úy lạo
uỵch
uyên bác
uyên thâm
uyển chuyển
ứ
ứ đọng
ứ huyết
ưa
ưa nhìn
ứa
ức
ức chế
ực
ưng
ưng thuận
ửng hồng
ứng biến
ứng dụng
ứng đáp
ứng khẩu
ứng phó
ứng thí
ước
ước chừng
ước định
ước độ
ước hẹn
ước lượng
ước mong
ước mơ
ước muốn
ước vọng
ướm
ươn
ươn hèn
ưỡn ẹo
ương ngạnh
ướp
ướp lạnh
ướt
ướt át
ướt đẫm
ưu ái
ưu điểm
ưu phiền
ưu sầu
ưu tiên
ưu việt
va
va li
va ni
và
vả
vả lại
vá
vá víu
vạ
vác
vạc
vạc dầu
vách
vạch
vạch trần
vai
vai trò
vài
vải
vại
vàm
van
van nài
van xin
vãn
vãn hồi
ván
vạn
vạn năng
vạn sự
vạn thọ
vạn vật
vang
vang lừng
vàng
vàng anh
vàng khè
vàng mười
vàng son
vàng tây
vàng y
vãng lai
váng
vành
vành đai
vành tai
vào
vào hùa
vào khoảng
vạt
vay
vảy
váy
vằm
văn bằng
văn cảnh
văn chương
văn đàn
văn hóa
văn học
văn kiện
văn minh
văn phong
văn phòng
văn phòng phẩm
văn thơ
văn vật
văn vẻ
vắn
vặn
vặn hỏi
văng
vẳng
vắng
vắng vẻ
vắt
vắt óc
vặt
vặt vãnh
vân
vân vân
vân vê
vần
vần thơ
vẩn đục
vẫn
vấn
vấn đáp
vấn đề
vấn vít
vận
vận chuyển
vận hành
vận tải
vận tốc
vâng
vâng lời
vấp
vất vả
vật
vật chất
vật liệu
vật lý học
vật thể
vẩu
vây
vây cánh
vầy
vẫy
vấy
vấy vá
vậy
vậy mà
vậy thì
ve
ve sầu
ve vẩy
vè
vẻ
vẻ vang
vẽ
vé
vén
vẹn toàn
vẹn vẽ
vèo
véo
véo von
vét
vẹt
vê
về
về hưu
vế
vệ
vệ binh
vệ sinh
vệ tinh
vênh
vênh váo
vểnh
vết
vết thương
vệt
vi khuẩn
vi ô lông
vi phạm
vi ta min
vi vút
vì
vì sao
vì thế
vỉ
vĩ đại
vĩ độ
vĩ tuyến
ví
ví như
ví thử
vị
vị chi
vị giác
vị kỷ
vị lai
vị ngữ
vị tha
vị trí
vỉa
vỉa hè
việc
việc làm
viêm
viên chức
viền
viễn cảnh
viễn thông
viện
viện cớ
viện lý
viện trợ
viếng thăm
viết
việt kiều
việt vị
vịn
vinh dự
vinh hạnh
vinh quang
vĩnh cửu
vĩnh viễn
vịnh
vít
vịt
vò
vò võ
vỏ
võ
võ nghệ
vó
vó câu
vóc dáng
voi
vòi
vòi voi
vòm
vòm canh
vong ân
vong linh
vòng
vòng hoa
vòng kiềng
vòng quanh
vòng vèo
võng
võng mạc
vọng
vọng gác
vọng tưởng
vót
vọt
vô biên
vô bổ
vô căn cứ
vô chủ
vô cơ
vô cực
vô danh
vô định
vô độ
vô giá
vô hại
vô hiệu
vô hình
vô ích
vô loại
vô lương tâm
vô lý
vô nghĩa
vô phép
vô sản
vô sinh
vô số
vô sự
vô tận
vô thần
vô thừa nhận
vô tình
vô tội
vô tư
vô tư lự
vô vị
vô ý thức
vồ vập
vỗ
vỗ béo
vỗ tay
vỗ về
vốc
vôi
vôi vữa
vội
vội vã
vồn vã
vốn
vống
vơ
vờ
vờ vịt
vở kịch
vỡ
vỡ lòng
vỡ mủ
vỡ nợ
vớ
vớ vẩn
vợ
vợ bé
với
vờn
vớt
vợt
vu khống
vu oan
vu qui
vu vơ
vù
vũ
vũ bão
vũ đài
vũ khúc
vũ nữ
vũ trụ
vú
vú em
vụ
vụ lợi
vua
vui
vùi
vun
vun trồng
vụn
vụn vặt
vung
vùng
vùng vằng
vùng vẫy
vũng
vụng
vuông
vuốt
vuốt ve
vụt
vừa
vừa lòng
vừa lúc
vừa mới
vừa tầm
vữa
vựa
vực
vừng
vững
vững bền
vững chắc
vươn
vườn
vườn bách thú
vườn cây
vượn
vương
vương vãi
vương vấn
vương víu
vướng
vượng
vượt
vứt
xa
xa cách
xa hoa
xa lạ
xa lánh
xa lộ
xa xăm
xa xỉ
xà
xà beng
xà bông
xà cừ
xà lách
xà lan
xà lim
xà nhà
xả
xả thân
xã
xã giao
xã hội
xã hội chủ nghĩa
xã hội học
xã luận
xã tắc
xá
xá tội
xạ hương
xạ kích
xạ thủ
xác
xác đáng
xác định
xác nhận
xác thực
xác xơ
xách
xài
xám
xám mặt
xám xịt
xán lạn
xanh
xanh biếc
xanh lá cây
xanh lơ
xanh xao
xao động
xao lãng
xao xuyến
xào
xào xạc
xảo
xảo quyệt
xáo trộn
xạo
xát
xay
xảy ra
xăm
xăm mình
xắn
xăng
xẵng
xắt
xấc
xấc xược
xâm chiếm
xâm lược
xâm nhập
xâm phạm
xấp xỉ
xâu
xâu xé
xấu
xấu hổ
xấu nết
xấu số
xấu xa
xấu xí
xây
xây dựng
xây mặt
xây xẩm
xe bò
xe buýt
xe cam nhông
xe cộ
xe cứu thương
xe du lịch
xe đạp
xe điện
xe đò
xe gắn máy
xe hỏa
xe tang
xe tắc xi
xẻ
xé
xem
xem xét
xen
xén
xéo
xẹo
xẹp
xét đoán
xét hỏi
xét xử
xê dịch
xê xích
xế
xếch
xếp
xếp đặt
xếp hàng
xếp thứ tự
xi
xi lanh
xi líp
xi măng
xi rô
xì
xì gà
xì xào
xỉ
xí nghiệp
xỉa
xích
xích đạo
xích đu
xích mích
xiếc
xiêm y
xiên
xiềng
xiết
xiêu
xiêu lòng
xiêu vẹo
xin
xin lỗi
xinê
xinh
xinh đẹp
xịt
xìu
xỉu
xíu
xo
xỏ
xó
xoa
xoã
xoá
xoài
xoàn
xoay
xoay quanh
xoay xở
xoáy
xoăn
xoắn xít
xóc
xoè
xoi
xoi mói
xóm
xóm giềng
xong
xong xuôi
xót
xót dạ
xô
xô bồ
xô đẩy
xô viết
xổ
xổ số
xốc
xốc vác
xốc xếch
xối
xối xả
xôn xao
xông
xốp
xơ
xơ xác
xờ
xới
xu
xu hướng
xu nịnh
xu thế
xu thời
xù
xú uế
xua đuổi
xuân
xuân phân
xuân thu
xuất
xuất bản
xuất cảng
xuất chinh
xuất chúng
xuất dương
xuất giá
xuất hành
xuất hiện
xuất phát
xuất sắc
xuất thân
xuất trình
xuất xứ
xúc
xúc cảm
xúc động
xúc giác
xúc phạm
xúc tiến
xúc xích
xúc xiểm
xuề xòa
xui
xủi bọt
xum họp
xúm
xung đột
xung khắc
xung phong
xung yếu
xuôi
xuôi chiều
xuôi dòng
xuôi vần
xuồng
xuổng
xuống
xụt xùi
xuyên
xuyên tạc
xuyến
xúyt
xúyt xoát
xử
xử hòa
xử lý
xử sự
xử thế
xử trảm
xử trí
xử tử
xứ
xứ sở
xưa
xưa kia
xức dầu
xưng danh
xưng hô
xưng tội
xứng đáng
xước
xương
xương cốt
xương rồng
xương sống
xương sườn
xương xẩu
xưởng
xướng
xướng danh
y
y học
y khoa
y nguyên
y phục
y sĩ
y tá
y tế
y viện
ỷ
ý
ý chí
ý định
ý kiến
ý muốn
ý nghĩ
ý nghĩa
ý niệm
ý thức
ý tưởng
ý vị
yểm
yểm hộ
yểm trợ
yếm
yếm dãi
yếm thế
yên
yên lặng
yên ổn
yên trí
yến
yến tiệc
yêng hùng
yết
yết hầu
yết kiến
yết thị
yêu
yêu cầu
yêu chuộng
yêu dấu
yêu kiều
yêu ma
yêu sách
yêu thuật
yêu tinh
yểu
yểu điệu
yếu
yếu điểm
yếu đuối
yếu lược
yếu nhân
yếu tố'''
