from industry_analysis import Industry_Analysis
import numpy as np
import pandas as pd 
import time 

# # 산업연관표 데이터 25개 분류 

# # 총
# data_2015 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2015/총/2015년 총거래표(25).xlsx')
# data_2016 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2016/총/2016년 총거래표(25).xlsx')
# data_2017 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2017/총/2017년 총거래표(25).xlsx')
# data_2018 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2018/총/2018년 총거래표(25).xlsx')
# data_2019 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2019/총/2019년 총거래표(25).xlsx')

# total_data_25 = [data_2015, data_2016, data_2017, data_2018, data_2019]

# # 국산 
# data_2015_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2015/국산/2015년 국산거래표(25).xlsx')
# data_2016_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2016/국산/2016년 국산거래표(25).xlsx')
# data_2017_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2017/국산/2017년 국산거래표(25).xlsx')
# data_2018_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2018/국산/2018년 국산거래표(25).xlsx')
# data_2019_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2019/국산/2019년 국산거래표(25).xlsx')

# total_data_25_domestic = [data_2015_domestic, data_2016_domestic, data_2017_domestic, data_2018_domestic, data_2019_domestic]



# # 산업연관표 데이터 5개 분류 

# # 맥용

# # 총 
# data_2015_5 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2015/총/2015년 총거래표(5).xlsx')
# data_2016_5 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2016/총/2016년 총거래표(5).xlsx')
# data_2017_5 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2017/총/2017년 총거래표(5).xlsx')
# data_2018_5 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2018/총/2018년 총거래표(5).xlsx')
# data_2019_5 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2019/총/2019년 총거래표(5).xlsx')

# total_data_5 = [data_2015_5, data_2016_5, data_2017_5, data_2018_5, data_2019_5]

# # 국산 
# data_2015_5_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2015/국산/2015년 국산거래표(5).xlsx')
# data_2016_5_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2016/국산/2016년 국산거래표(5).xlsx')
# data_2017_5_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2017/국산/2017년 국산거래표(5).xlsx')
# data_2018_5_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2018/국산/2018년 국산거래표(5).xlsx')
# data_2019_5_domestic = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/2019/국산/2019년 국산거래표(5).xlsx')

# total_data_5_domestic = [data_2015_5_domestic, data_2016_5_domestic, data_2017_5_domestic, data_2018_5_domestic, data_2019_5_domestic]


# # 고용표 
# employ_data_5 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/고용표_최종(5).xlsx')
# employ_data_25 = pd.read_excel('/Users/dongyokim/main/jupyter/2022:Summer/프로젝트/고용표_최종(25).xlsx')






# if __name__ == '__main__':


#     # industry_analysis = Industry_Analysis(total_data_5, total_data_5_domestic, employ_data_5, 5, 2015)
#     industry_analysis = Industry_Analysis(total_data_25, total_data_25_domestic, employ_data_25, 25, 2015)


#     special_list = ['공간정보 관련 제조업', '공간정보 관련 도매업', '공간정보 관련 출판 및 정보서비스업', '공간정보 관련 기술서비스업', '공간정보 관련 교육서비스업', '공간정보 관련 협회 및 단체']
#     # special_list = ['공간정보산업']



    # industry_analysis.add_special_industry_list(special_list)



    # industry_analysis.total_industry_scale()