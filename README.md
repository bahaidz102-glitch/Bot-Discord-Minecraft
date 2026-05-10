# Minecraft Discord Bot

Bot Discord Python theo dõi server Minecraft 24/7.

Tự động thông báo khi server bật/tắt, kiểm tra người chơi và pick role.

Được tạo bởi BahaiDZ (chủ sever minectaft Gosling)

---

## Mục lục

- [Tính năng](#tinh-nang)
- [Yêu cầu](#yeu-cau)
- [Cài đặt](#cai-dat)
- [Hướng dẫn cấu hình](#huong-dan-cau-hinh)
- [Chạy bot](#chay-bot)
- [Lệnh bot](#lenh-bot)
- [Cấu trúc thư mục](#cau-truc-thu-muc)
- [Thư viện sử dụng](#thu-vien-su-dung)

---

## Tính năng

- Lệnh `!status` : Kiểm tra trạng thái server (online/offline, số người chơi, ping, version)
- Lệnh `!players` : Xem danh sách người chơi đang online
- Nút pick role cho người chơi (thêm/gỡ role qua nút bấm)
- Lệnh `!help` : Hiển thị menu trợ giúp

---

## Yêu cầu

- Python 3.8 trở lên
- pip (Python package manager)
- Discord Bot Token
- Server Minecraft Java Edition

---

## Cài đặt

### Bước 1: Tải code

Mở Terminal và chạy từng dòng:

```bash
git clone https://github.com/bahaidz102-glitch/Bot-Discord-Minecraft.git
```

```bash
cd Bot-Discord-Minecraft/mc-discord
```

### Bước 2: Cài thư viện

Cách 1 - Cài trực tiếp:

```bash
pip install discord.py mcstatus

Sau khi cài xong, mỗi lần chạy bot phải kích hoạt venv trước:

```bash
source venv/bin/activate
```

---

## Hướng dẫn cấu hình

### Bước 1: Mở file config.py

Trong thư mục bot, mở file `config.py` bằng Notepad hoặc VS Code.

### Bước 2: Điền thông tin

Bạn sẽ thấy các dòng bên dưới. Hãy điền thông tin của bạn vào:

```python
# ========== DISCORD BOT ==========
TOKEN = "TOKEN DISCORD"
PREFIX = "!"
BOT_NAME = "NAME BOT"

# ========== MINECRAFT SERVER ==========
SERVER_IP = "IP SEVER MINECRAFT"
SERVER_PORT = PORT SEVER MINECRAFT
CHECK_INTERVAL = 30

# ========== KENH AUTO THONG BAO ==========
CHANNEL_ID = ID CHANNEL DISCORD

# ========== PICK ROLE ==========
ROLE_ID = ID ROLE DISCORD
ROLE_EMOJI = "NAME EMOJI"
ROLE_LABEL = "COLOR"
```

### Bước 3: Giải thích từng thông số

| Thông số | Mô tả | Ví dụ |
|----------|-------|-------|
| TOKEN | Token bot Discord | "MTIzNDU2Nzg5M..." |
| PREFIX | Ký tự đứng trước lệnh | "!" |
| BOT_NAME | Tên hiển thị của bot | "Minecraft" |
| SERVER_IP | IP hoặc domain server Minecraft | "play.example.com" |
| SERVER_PORT | Port server Minecraft | 25565 |
| CHECK_INTERVAL | Thời gian kiểm tra tự động (giây) | 30 |
| CHANNEL_ID | ID kênh Discord để bot gửi thông báo | 1234567890 |
| ROLE_ID | ID role Discord để gán cho người chơi | 9876543210 |
| ROLE_EMOJI | Emoji hiển thị trên nút pick role | "🟢" |
| ROLE_LABEL | Nhãn hiển thị trên nút pick role | "Xanh" |

---

## Hướng dẫn lấy Token và ID

### Cách lấy Discord Bot Token

1. Vào Discord Developer Portal: https://discord.com/developers/applications
2. Nhấn nút **New Application** (góc phải trên)
3. Đặt tên cho bot, nhấn **Create**
4. Chọn tab **Bot** (menu bên trái)
5. Nhấn **Add Bot** > **Yes, do it!**
6. Nhấn **Reset Token** > **Copy**
7. Dán token vào `TOKEN` trong file `config.py`

> **Lưu ý:** Token chỉ hiện 1 lần. Nếu mất phải Reset lại.

### Cách bật Message Content Intent

1. Vào Discord Developer Portal > Chọn bot của bạn
2. Tab **Bot** > Cuộn xuống **Privileged Gateway Intents**
3. Bật **Message Content Intent**
4. Nhấn **Save Changes**

### Cách lấy Channel ID

1. Mở Discord > Vào **Cài đặt** (biểu tượng răng cưa)
2. Chọn **Advanced** (bên trái)
3. Bật **Developer Mode**
4. Chuột phải vào kênh muốn bot gửi thông báo
5. Chọn **Copy ID**
6. Dán vào `CHANNEL_ID` trong file `config.py`

### Cách lấy Role ID

1. Discord Server > **Server Settings** > **Roles**
2. Tạo role mới hoặc chọn role có sẵn
3. Chuột phải vào role > **Copy ID**
4. Dán vào `ROLE_ID` trong file `config.py`

### Cách mời bot vào server

1. Discord Developer Portal > Chọn bot > Tab **OAuth2** > **URL Generator**
2. Chọn scope: `bot`
3. Chọn permissions: `Administrator` (hoặc chọn thủ công)
4. Copy URL hiện ra, dán vào trình duyệt
5. Chọn server > **Authorize**

---

## Chạy bot

### Cách 1: Chạy trực tiếp

```bash
cd mc-bot
```

```bash
python3 bot.py
```

Nếu dùng venv:

```bash
source venv/bin/activate
```

```bash
python3 bot.py
```

Khi thấy dòng này là thành công:

```
Bot: Minecraft#1234
Server: abc.com:25565
Check: 30s
Kenh auto: 1234567890
```

## Lệnh bot

| Lệnh | Chức năng |
|------|-----------|
| `!status` | Kiểm tra trạng thái server Minecraft |
| `!st` | Viết tắt của `!status` |
| `!players` | Xem danh sách người chơi đang online |
| `!pl` | Viết tắt của `!players` |
| `!setup_role` | (Admin) Tạo nút pick role trong kênh |
| `!help` | Hiển thị danh sách lệnh |
| `!h` | Viết tắt của `!help` |

---

## Cấu trúc thư mục

```
mc-bot/
├── bot.py              # File chính chạy bot
├── config.py           # File cấu hình (không đẩy lên GitHub)
├── config.example.py   # File cấu hình mẫu
├── .gitignore          # File bỏ qua khi push
├── README.md           # File hướng dẫn này
└── cogs/
    ├── __init__.py     
    ├── minecraft.py    # Lệnh 
    └── pick_role.py    # Nút pick role
```

---

## Lỗi thường gặp

### Bot không online

**Nguyên nhân:** Token sai hoặc chưa bật Intent.

**Cách sửa:**

1. Kiểm tra `TOKEN` trong `config.py` đã đúng chưa
2. Vào Discord Developer Portal > Bot > Bật **Message Content Intent**
3. Nhấn **Save Changes**
4. Chạy lại bot

### Bot không gửi thông báo tự động

**Nguyên nhân:** Sai Channel ID hoặc thiếu quyền.

**Cách sửa:**

1. Kiểm tra `CHANNEL_ID` trong `config.py`
2. Đảm bảo bot có quyền `Send Messages` và `Embed Links` trong kênh đó
3. Xem terminal có dòng `Không tìm thấy kênh` không

### Lệnh không hoạt động

**Nguyên nhân:** Dùng sai prefix hoặc chưa bật Intent.

**Cách sửa:**

1. Dùng `!status`, không dùng `/status`
2. Kiểm tra `PREFIX` trong `config.py` (mặc định là `!`)
3. Bật **Message Content Intent** trong Discord Developer Portal

### Không ping được server Minecraft

**Nguyên nhân:** Sai IP, Port hoặc server tắt.

**Cách sửa:**

1. Kiểm tra `SERVER_IP` và `SERVER_PORT`
2. Thử ping server từ máy khác
3. Kiểm tra tường lửa có chặn không

### Pick role không hoạt động

**Nguyên nhân:** Chưa tạo nút hoặc sai Role ID.

**Cách sửa:**

1. Dùng lệnh `!setup_role` để tạo nút
2. Kiểm tra `ROLE_ID` đã đúng chưa
3. Bot cần quyền `Manage Roles`
4. Role của bot phải cao hơn role cần gán

---

## Thư viện sử dụng

| Thư viện | Mục đích |
|----------|----------|
| discord.py | Kết nối Discord API |
| mcstatus | Ping server Minecraft |
| asyncio | Xử lý bất đồng bộ |
| json | Đọc/ghi dữ liệu |
| datetime | Xử lý thời gian |

---

## Liên hệ

Nếu có lỗi hoặc cần trợ giúp, liên hệ **OK** hoặc tạo Issue trên GitHub.

---

**Được tạo bởi Bahai 2026**
```
