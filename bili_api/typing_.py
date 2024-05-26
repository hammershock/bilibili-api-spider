import re
from typing import TypedDict, List, Dict, Any, Optional


class Rights(TypedDict):
    bp: int  # bp 许可
    elec: int  # 充电许可
    download: int  # 下载许可
    movie: int  # 电影许可
    pay: int  # 付费许可
    hd5: int  # 高清许可
    no_reprint: int  # 禁止转载
    autoplay: int  # 自动播放
    ugc_pay: int  # 用户生成内容付费
    is_cooperation: int  # 合作视频
    ugc_pay_preview: int  # 用户生成内容付费预览
    no_background: int  # 无背景
    clean_mode: int  # 清洁模式
    is_stein_gate: int  # 是斯坦因之门
    is_360: int  # 是360度视频
    no_share: int  # 禁止分享
    arc_pay: int  # 拱门支付
    free_watch: int  # 免费观看


class Owner(TypedDict):
    mid: int  # 用户ID
    name: str  # 用户名
    face: str  # 用户头像


class Stat(TypedDict):
    aid: int  # 视频ID
    view: int  # 观看数
    danmaku: int  # 弹幕数
    reply: int  # 评论数
    favorite: int  # 收藏数
    coin: int  # 硬币数
    share: int  # 分享数
    now_rank: int  # 当前排名
    his_rank: int  # 历史最高排名
    like: int  # 点赞数
    dislike: int  # 点踩数
    evaluation: str  # 评价
    vt: int  # VT


class ArgueInfo(TypedDict):
    argue_msg: str  # 争议信息
    argue_type: int  # 争议类型
    argue_link: str  # 争议链接


class Dimension(TypedDict):
    width: int  # 宽度
    height: int  # 高度
    rotate: int  # 旋转角度


class Page(TypedDict):
    cid: int  # 视频CID
    page: int  # 页码
    from_: str  # 来源
    part: str  # 部分
    duration: int  # 时长
    vid: str  # 视频ID
    weblink: str  # 网络链接
    dimension: Dimension  # 尺寸
    first_frame: str  # 第一帧


class SubtitleAuthor(TypedDict):
    mid: int  # 作者ID
    name: str  # 作者名
    sex: str  # 性别
    face: str  # 头像
    sign: str  # 签名
    rank: int  # 等级
    birthday: int  # 生日
    is_fake_account: int  # 是否是假账号
    is_deleted: int  # 是否被删除
    in_reg_audit: int  # 是否在注册审核中
    is_senior_member: int  # 是否是高级会员


class UserGarb(TypedDict):
    url_image_ani_cut: str  # 动态剪切图URL


class VideoInfo(TypedDict):
    bvid: str  # 视频BVID
    aid: int  # 视频AID
    videos: int  # 视频数量
    tid: int  # 类型ID
    tname: str  # 类型名
    copyright: int  # 版权
    pic: str  # 图片URL
    title: str  # 标题
    pubdate: int  # 发布日期
    ctime: int  # 创建时间
    desc: str  # 描述
    desc_v2: Optional[List[Dict[str, Any]]]  # 描述版本2
    state: int  # 状态
    duration: int  # 时长
    rights: Rights  # 权限
    owner: Owner  # 拥有者
    stat: Stat  # 统计信息
    argue_info: ArgueInfo  # 争议信息
    dynamic: str  # 动态
    cid: int  # CID
    dimension: Dimension  # 尺寸
    premiere: Optional[Any]  # 首映
    teenage_mode: int  # 青少年模式
    is_chargeable_season: bool  # 是否是付费季
    is_story: bool  # 是否是故事
    is_upower_exclusive: bool  # 是否独家
    is_upower_play: bool  # 是否播放
    is_upower_preview: bool  # 是否预览
    enable_vt: int  # 启用VT
    vt_display: str  # VT显示
    no_cache: bool  # 无缓存
    pages: List[Page]  # 页码
    subtitle: Dict[str, Any]  # 字幕
    is_season_display: bool  # 是否显示季
    user_garb: UserGarb  # 用户装饰
    honor_reply: Dict[str, Any]  # 荣誉回复
    like_icon: str  # 点赞图标
    need_jump_bv: bool  # 是否需要跳转BV
    disable_show_up_info: bool  # 禁用显示UP信息
    is_story_play: int  # 是否播放故事


class Tag(TypedDict):
    tag_id: int  # 标签ID
    tag_name: str  # 标签名
    music_id: str  # 音乐ID
    tag_type: str  # 标签类型
    jump_url: str  # 跳转URL


class IpInfo(TypedDict):
    ip: str  # IP 地址
    zone_ip: str  # 区域 IP
    zone_id: int  # 区域 ID
    country: str  # 国家
    province: str  # 省份
    city: str  # 城市


class LevelInfo(TypedDict):
    current_level: int  # 当前等级
    current_min: int  # 当前等级的最小经验值
    current_exp: int  # 当前经验值
    next_exp: int  # 下一等级所需经验值
    level_up: int  # 升级所需经验值


class VipLabel(TypedDict):
    path: str  # 路径
    text: str  # 文本
    label_theme: str  # 标签主题
    text_color: str  # 文本颜色
    bg_style: int  # 背景样式
    bg_color: str  # 背景颜色
    border_color: str  # 边框颜色
    use_img_label: bool  # 是否使用图片标签
    img_label_uri_hans: str  # 简体中文图片标签 URI
    img_label_uri_hant: str  # 繁体中文图片标签 URI
    img_label_uri_hans_static: str  # 简体中文静态图片标签 URI
    img_label_uri_hant_static: str  # 繁体中文静态图片标签 URI


class Vip(TypedDict):
    type: int  # VIP 类型
    status: int  # VIP 状态
    due_date: int  # 到期日期
    vip_pay_type: int  # VIP 支付类型
    theme_type: int  # 主题类型
    label: VipLabel  # VIP 标签
    avatar_subscript: int  # 头像附加标识
    nickname_color: str  # 昵称颜色
    role: int  # 角色
    avatar_subscript_url: str  # 头像附加标识 URL
    tv_vip_status: int  # TV VIP 状态
    tv_vip_pay_type: int  # TV VIP 支付类型
    tv_due_date: int  # TV VIP 到期日期
    avatar_icon: Dict[str, Any]  # 头像图标


class SubtitleType(TypedDict):
    id: int  # 字幕ID
    lan: str  # 语言
    lan_doc: str  # 语言文档
    is_lock: bool  # 是否锁定
    subtitle_url: str  # 字幕URL, 不包含协议头https:
    type: int  # 字幕类型
    id_str: str  # 字幕ID字符串
    ai_type: int  # AI类型
    ai_status: int  # AI状态
    author: SubtitleAuthor  # 作者


class SubtitleInfo(TypedDict):
    allow_submit: bool
    lan: str
    lan_doc: str
    subtitles: List[SubtitleType]


class VideoDetails(TypedDict):
    aid: int  # 视频 AID
    bvid: str  # 视频 BVID
    allow_bp: bool  # 是否允许 BP
    no_share: bool  # 是否禁止分享
    cid: int  # 视频 CID
    max_limit: int  # 最大限制
    page_no: int  # 页码
    has_next: bool  # 是否有下一页
    ip_info: IpInfo  # IP 信息
    login_mid: int  # 登录用户 MID
    login_mid_hash: str  # 登录用户 MID 哈希
    is_owner: bool  # 是否是拥有者
    name: str  # 名称
    permission: str  # 权限
    level_info: LevelInfo  # 等级信息
    vip: Vip  # VIP 信息
    answer_status: int  # 回答状态
    block_time: int  # 阻止时间
    role: str  # 角色
    last_play_time: int  # 上次播放时间
    last_play_cid: int  # 上次播放 CID
    now_time: int  # 当前时间
    online_count: int  # 在线人数
    need_login_subtitle: bool  # 是否需要登录字幕
    subtitle: SubtitleInfo  # 字幕信息
    view_points: List[Any]  # 观看点
    preview_toast: str  # 预览提示
    options: Dict[str, bool]  # 选项
    guide_attention: List[Any]  # 引导关注
    jump_card: List[Any]  # 跳转卡片
    operation_card: List[Any]  # 操作卡片
    online_switch: Dict[str, str]  # 在线开关
    fawkes: Dict[str, int]  # 福克斯配置
    show_switch: Dict[str, bool]  # 显示开关
    bgm_info: Optional[Any]  # 背景音乐信息
    toast_block: bool  # 是否弹出阻止
    is_upower_exclusive: bool  # 是否独家播放
    is_upower_play: bool  # 是否播放
    is_ugc_pay_preview: bool  # 是否是用户生成内容付费预览
    elec_high_level: Dict[str, Any]  # 高级电力信息
    disable_show_up_info: bool  # 禁用显示 UP 信息


class SubtitleItem(TypedDict):
    from_: float  # 字幕开始时间
    to: float  # 字幕结束时间
    sid: int  # 字幕ID
    location: int  # 字幕位置
    content: str  # 字幕内容
    music: float  # 背景音乐音量


class SubtitleData(TypedDict):
    font_size: float  # 字体大小
    font_color: str  # 字体颜色
    background_alpha: float  # 背景透明度
    background_color: str  # 背景颜色
    Stroke: str  # 描边效果
    type: str  # 字幕类型
    lang: str  # 语言
    version: str  # 版本
    body: List[SubtitleItem]  # 字幕内容列表


BVID_PATTERN = re.compile(r'^BV[0-9A-Za-z]{10}$')
