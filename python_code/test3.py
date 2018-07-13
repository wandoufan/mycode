# -*- coding: UTF-8 -*-
import fastText
import jieba
import re
import json
import traceback
from nlp_demo import config_default
from nlp_demo.text_classification.base_model import BaseModel


class FastTextClassificationModel(BaseModel):
    """文本分类模型"""
    def __init__(self, model_path, **params):
        """初始化"""
        self.model_path = model_path
        self.params = params
        self.classify_dict = {
            0: '未知类别',
            10: '财经', 11: '旅行', 12: '美食', 13: '汽车', 14: '历史', 15: '教育', \
            16: '育儿', 17: '时尚', 18: '娱乐', 19: '科技数码', 20: '健康', 21: '体育', \
            22: '星座运势', 23: '动漫', 24: '情感', 25: '互联网', 26: '军事', 27: '休闲生活', \
            28: '商业职场', 1001: '股票', 1002: '基金', 1003: '期货', 1004: '外汇', 1005: '理财', \
            1006: '油价', 1007: 'GDP', 1008: 'IPO', 1009: '央行', 1010: '证监会', 1011: 'A股', \
            1012: '港股', 1013: '美股', 1014: '金融', 1101: '旅游攻略', 1102: '国内游', \
            1103: '出境游', 1104: '自驾游', 1105: '蜜月游', 1106: '周边游', 1107: '穷游', \
            1108: '背包旅行', 1109: '摄影旅行', 1110: '海岛游', 1111: '三亚旅游', 1112: '北京旅游', \
            1113: '日本旅游', 1114: '泰国旅游', 1115: '台湾旅游', 1201: '养生食谱', \
            1202: '减肥食谱', 1203: '美食', 1204: '家常菜', 1205: '饮食禁忌', 1206: '煲汤', \
            1207: '火锅', 1208: '甜点', 1209: '西餐', 1210: '烧烤', 1211: '川菜', 1212: '韩国料理', \
            1213: '湘菜', 1214: '粤菜', 1215: '鲁菜', 1216: '老人饮食', 1301: '新车', 1302: '购车', \
            1303: '汽车评测', 1304: '汽车保养', 1305: '开车技巧', 1306: '汽车改装', \
            1307: '新能源车', 1308: 'SUV', 1309: '女司机', 1310: '车模', 1311: '汽车美容', \
            1312: '车展', 1313: '宝马', 1314: '奔驰', 1315: '奥迪', 1316: '大众汽车', \
            1317: '丰田', 1318: '通用汽车', 1400: '历史', 1401: '毛泽东', 1402: '蒋介石', \
            1403: '二战', 1404: '一战', 1405: '古代', 1406: '明朝', 1407: '清朝', 1408: '历史视频', \
            1409: '老照片', 1410: '唐朝', 1411: '宋朝', 1412: '汉朝', 1413: '春秋战国', 1414: '军史', \
            1415: '日本历史', 1416: '美国历史', 1417: '世界历史', 1500: '高考', 1501: '教师', 1502: '大学生', \
            1503: '考研', 1504: '中考', 1505: '初中', 1506: '家庭教育', 1507: '职业规划', \
            1508: '大学', 1509: '小学', 1510: '幼儿教育', 1511: '求职', 1512: '研究生', \
            1513: '高中留学', 1600: '孕妇', 1601: '宝宝', 1602: '儿童健康', 1603: '孕期健康', \
            1604: '亲子教育', 1605: '胎儿', 1606: '哺乳期', 1607: '宝宝营养', 1608: '分娩', \
            1609: '幼儿教育', 1610: '辅食', 1611: '备孕', 1612: '生男生女', 1613: '剖腹产', \
            1700: '穿衣搭配', 1701: '时装周', 1702: '健身', 1703: '明星时尚', 1704: '型男', \
            1705: '美容', 1706: '化妆', 1707: '模特', 1708: '街拍', 1709: '发型', 1710: '美体', \
            1711: '奢侈品', 1712: '时装', 1713: '配饰', 1800: '八卦爆料', 1801: '明星', \
            1802: '综艺', 1803: '电影', 1804: '电视剧', 1805: '音乐', 1806: '动漫', \
            1807: '影评', 1808: '内地娱乐', 1809: '港台娱乐', 1810: '日韩娱乐', 1811: '欧美娱乐', \
            1812: '韩剧', 1813: '日剧', 1814: '美剧', 1815: '英剧', 1816: '小视频', 1900: '人工智能', \
            1901: '数码', 1902: '互联网', 1903: '手机', 1904: '创业投资', 1905: 'IT', 1906: '穿戴设备', \
            1907: '移动互联', 1908: '电商', 1909: 'iPhone', 1910: '人机大战', 1911: '通信业', \
            2000: '中医', 2001: '疾病', 2002: '养生', 2003: '健身', 2004: '男性健康', \
            2005: '女性健康', 2006: '心理健康', 2007: '癌症', 2008: '糖尿病', 2009: '妇科', \
            2010: '感冒', 2011: '失眠', 2012: '针灸', 2013: '口腔', 2014: '颈椎', 2100: 'NBA', \
            2101: 'CBA', 2102: '围棋', 2103: '足球', 2104: '篮球', 2105: '中超', 2106: '英超', \
            2107: '德甲', 2108: '意甲', 2109: '西甲', 2110: '欧冠', 2111: '亚冠', 2112: '中国足球', \
            2113: '羽毛球', 2114: '乒乓', 2115: '网球', 2116: '排球', 2200: '星座', 2201: '生肖', \
            2202: '算命', 2203: '风水', 2204: '血型', 2205: '解梦', 2206: '占卜', 2300: '二次元', \
            2301: '动画', 2302: '漫画', 2303: 'Cosplay', 2304: '动漫电影', 2305: '动漫周边', \
            2306: '动漫经济', 2307: 'ACG', 2400: '恋爱', 2401: '婚姻', 2402: '失恋', \
            2403: '情感心理', 2404: '剩男剩女', 2405: '同性婚姻', 2406: '暗恋', 2407: '求婚', \
            2408: '婆媳', 2409: '婚礼', 2410: '单身', 2500: '电商', 2501: '移动互联', \
            2502: '互联网创业', 2503: '互联网金融', 2504: '社交网络', 2505: '创业投资', \
            2506: 'O2O', 2507: '移动支付', 2508: 'BAT', 2509: '大数据', 2510: '互联网思维', \
            2511: '众筹', 2600: '南海', 2601: '航母', 2602: '解放军', 2603: '军史', 2604: '武器', \
            2605: '中国军事', 2606: '国际军事', 2607: '核武器', 2608: '坦克', 2609: '无人机', \
            2610: '特种部队', 2611: '反恐', 2612: '钓鱼岛', 2700: '摄影', 2701: '宠物', \
            2702: '唯美', 2703: '奇闻趣事', 2704: '饮茶', 2705: '钓鱼', 2706: '瑜伽', 2707: '骑行', \
            2708: '手工', 2709: '生活', 2710: '户外', 2711: '太极拳', 2712: '书法', 2713: '潜水', \
            2800: '职业规划', 2801: '求职', 2802: '创业投资', 2803: '企业管理', 2804: '营销', \
            2805: '程序员', 2806: '产品经理', 2807: '公关', 2808: '视觉设计', 2809: '金融业', \
            2810: '传媒行业', 2811: '教育行业', 2812: '旅游业', 2813: '医药行业', 2814: '电商行业', \
            2815: '律师行业', 2816: '小本创业', 2817: '学生创业', 2818: '餐饮业'
        }
        self.model = self.load()

    def load(self):
        """加载训练好的模型"""
        model = fastText.load_model(self.model_path)
        return model

    def _load(self):
        pass

    def train(self, train_data):
        classifier = fastText.train_supervised(input=train_data, epoch=50)
        return classifier

    def predict(self, title, content):
        """
        预测
        :param title: 文本标题
        :param content:文本内容
        :return:
        """
        # 定义返回格式
        ret_json = {'code': 0, 'message': 'ok'}
        # 标题校验
        title_flag_preverify, title_msg_preverify = self._title_preverify(title)
        if not title_flag_preverify:  # 预校验失败
            ret_json['code'] = 101
            ret_json['message'] = title_msg_preverify
            return json.dumps(ret_json)
        # 内容校验
        content_flag_preverify, content_msg_preverify = self._content_preverify(content)
        if not content_flag_preverify:  # 预校验失败
            ret_json['code'] = 101
            ret_json['message'] = content_msg_preverify
            return json.dumps(ret_json)
        try:
            if not title:
                title = ''
            # 数据预处理
            text_list = [title + content]
            text = [' '.join(list(jieba.cut(i.strip()))) for i in text_list]
            # 模型预测
            pred_labels, pred_probs = self.model.predict(text, k=3)
            # 结果组装
            classes_list = []
            for i in range(len(pred_labels[0])):
                result_dict = {}
                pred_label = re.sub(r'__label__', '', pred_labels[0][i])
                pred_prob = pred_probs[0][i]
                result_dict['code'] = pred_label
                result_dict['score'] = pred_prob
                id_father = int(str(pred_label)[:2])
                classify_father = self.classify_dict[id_father]
                classify_child = self.classify_dict[pred_label]
                result_dict['name'] = classify_father + '_' + class_child
                classes_list.append(result_dict)

            ret_json = {'code': 0, 'message': 'ok',
                    'data': {'classes': classes_list}}
            return json.dumps(ret_json)
            # return self._return_format(pred_label, round(pred_prob, 4))
        except Exception:
            traceback.print_exc()
            ret_json['code'] = 102
            ret_json['message'] = '请求超时'
        return json.dumps(ret_json)

    def _return_format(self, pred_label, pred_prob):
        """返回值格式化"""
        # 如果概率低于设定阈值，则预测为默认类别
        config = config_default.configs
        unknown_class_prob = config['classify']['unknown_class_prob']
        if pred_prob < unknown_class_prob:
            pred_label = '未知类别'
        ret_json = {'code': 0, 'message': 'ok',
                    'data': {'class': self.classify_dict[pred_label],
                             'name': pred_label,
                             'score': pred_prob}}
        return json.dumps(ret_json)

    def _title_preverify(self, title):
        """
        文本校验
        :param title:文本标题
        :return:
        """
        config = config_default.configs
        title_max_length = config['classify']['title_max_length']
        if title:
            title_strip = title.strip()
            if len(title_strip) == 0:
                return True, None
            elif len(title_strip) > title_max_length:
                return False, '文本标题最长为{}'.format(title_max_length)
            else:
                return True, None
        else:
            return True, None

    def _content_preverify(self, content):
        """
        文本内容校验
        :param content:文本内容
        :return:
        """
        config = config_default.configs
        content_max_length = config['classify']['content_max_length']
        if content:
            content_strip = content.strip()
            if len(content_strip) == 0:
                return False, '文本内容不能为空'
            elif len(content_strip) > content_max_length:
                return False, '文本内容最长为{}'.format(content_max_length)
            else:
                return True, None
        else:
            return False, '文本内容不能为空'

