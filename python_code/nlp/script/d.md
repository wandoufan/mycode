测试文件：cityu_test_simple.utf8

./main.py cws baidu -i /data/home/xingyifan/nlp_project/segment_test2/a.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/b.utf8
-------------------------------------------------------------------------------
./main.py cws baidu -i /data/share/corpus/cws/icwb2-data/testing/cityu_test_simple.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/baidu-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/baidu-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/baidu-cityu-test.seg > /data/home/xingyifan/nlp_project/segment_test2/baidu_result_4.txt
-------------------------------------------------------------------------------
./main.py cws boson -i /data/share/corpus/cws/icwb2-data/testing/cityu_test_simple.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/boson-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/boson-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/boson-cityu-test.seg > /data/home/xingyifan/nlp_project/segment_test2/boson_result_4.txt
------------------------------------------------------------------------------
./main.py cws han -i /data/share/corpus/cws/icwb2-data/testing/cityu_test_simple.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/han-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/han-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/han-cityu-test.seg > /data/home/xingyifan/nlp_project/segment_test2/han_result_4.txt
-------------------------------------------------------------------------------
./main.py cws nlpir -i /data/share/corpus/cws/icwb2-data/testing/cityu_test_simple.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/nlpir-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/nlpir-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/nlpir-cityu-test.seg > /data/home/xingyifan/nlp_project/segment_test2/nlpir_result_4.txt
-------------------------------------------------------------------------------

./main.py cws yunfumatching -i /data/share/corpus/cws/icwb2-data/testing/cityu_test_simple.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/yunfumatching-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/yunfumatching-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/yunfumatching-cityu-test.seg > /data/home/xingyifan/nlp_project/segment_test2/yunfumatching_result_4.txt
-------------------------------------------------------------------------------

./main.py cws thulac -i /data/share/corpus/cws/icwb2-data/testing/cityu_test_simple.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/thulac-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/thulac-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/thulac-cityu-test.seg > /data/home/xingyifan/nlp_project/segment_test2/thulac_result_4.txt
-------------------------------------------------------------------------------

./main.py cws ltp -i /data/share/corpus/cws/icwb2-data/testing/cityu_test_simple.utf8 -o /data/home/xingyifan/nlp_project/segment_test2/ltp-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/ltp-cityu-test.seg

./evaluate/cws.py /data/share/corpus/cws/icwb2-data/gold_cn/cityu_testing_gold_cn.txt /data/home/xingyifan/nlp_project/segment_test2/ltp-cityu-test.seg > /data/home/xingyifan/nlp_project/segment_test2/ltp_result_4.txt
-------------------------------------------------------------------------------


