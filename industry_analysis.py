import pandas as pd
import numpy as np
import time


class Industry_Analysis():
    """
    0.1 초기 설정 
    """

    def __init__(self, total_data, total_data_domestic, employ_data, metrix_num, year):
        self.total_data = total_data
        self.total_data_domestic = total_data_domestic
        self.employ_data = employ_data
        self.metrix_num = metrix_num
        self.year = year
        self.special_industry_list = []

        for i in range(5):
            self.total_data[i].rename(
                columns={'Unnamed: 0': '상품분류'}, inplace=True)
            self.total_data[i].set_index('상품분류', inplace=True)

            self.total_data_domestic[i].rename(
                columns={'Unnamed: 0': '상품분류'}, inplace=True)
            self.total_data_domestic[i].set_index('상품분류', inplace=True)

        self.employ_data.rename(columns={'Unnamed: 0': '상품분류'}, inplace=True)
        self.employ_data.set_index('상품분류', inplace=True)

        self.index_name = list(total_data[0].index.values[:metrix_num])

    """
    0.2. 특정 산업 list 추가 
    """

    def add_special_industry_list(self, industry_list):
        self.special_industry_list.extend(industry_list)

        print(f">>> Num of IndustryGroups: {len(self.special_industry_list)}")

    """
    1. 산업 구조 
    """

    # 1) 산업 구조의 변화

    # 2015~2019년 전체 산업 규모
    def total_industry_scale(self):
        data_list = []
        year = self.year
        for data in self.total_data:
            # 중간수요
            middle_demand = data.loc['중간투입계', '중간수요계']

            # 최종수요
            final_demand = data.loc['중간투입계', '최종수요계']

            # 총수요
            total_demand = data.loc['중간투입계', '총수요계']

            # 중간 투입
            middle_input = data.loc['중간투입계', '중간수요계']

            # 부가가치
            added_value = data.loc['부가가치계', '중간수요계']

            # 수입계
            total_income = data.loc['중간투입계', '수입계']

            # 총공급
            total_supply = data.loc['중간투입계', '총공급계']

            data_list.append([str(year), middle_demand, final_demand, total_demand,
                             middle_input, added_value, total_income, total_supply])
            year += 1

        industry_scale_df = pd.DataFrame(data=data_list, columns=[
                                         '연도', '중간수요', '최종수요', '총수요', '중간투입', '부가가치', '수입계', '총공급'])

        industry_scale_df.set_index('연도', inplace=True)

        return industry_scale_df

    # 1) 산업 구조의 변화

    # 연도별 전체 산업 규모
    def industry_scale(self):
        total_struc_data = []

        for data in self.total_data:

            df = pd.DataFrame(data=[], columns=[
                              '산업명', '중간수요', '최종수요', '총수요', '중간투입', '부가가치', '총투입(=총산출)', '수입계', '총공급'])

            # 산업별 이름
            industry_name = self.index_name[:self.metrix_num]
            industry_name.append('총계')
            industry_name = np.array(industry_name)
            df['산업명'] = industry_name

            df.set_index('산업명', inplace=True)

            # 산업별 중간수요
            middle_demand = data.loc[:'중간투입계', '중간수요계'].values
            df['중간수요'] = middle_demand

            # 산업별 최종수요
            final_demand = data.loc[:'중간투입계', '최종수요계'].values
            df['최종수요'] = final_demand

            # 산업별 총수요계
            total_demand = data.loc[:'중간투입계', '총수요계'].values
            df['총수요'] = total_demand

            # 산업별 중간투입
            middle_input = data.loc['중간투입계', :'중간수요계'].values
            df['중간투입'] = middle_input

            # 산업별 부가가치
            added_value = data.loc['부가가치계', :'중간수요계'].values
            df['부가가치'] = added_value

            # 산업별 총투입계
            total_input = data.loc['총투입계', :'중간수요계'].values
            df['총투입(=총산출)'] = total_input

            # 산업별 수입계
            total_income = data.loc[:'중간투입계', '수입계'].values
            df['수입계'] = total_income

            # 산업별 총공급
            total_supply = data.loc[:'중간투입계', '총공급계'].values
            df['총공급'] = total_supply

            total_struc_data.append(df)

        # 산업 비중(%)
        total_struc_data_per = []
        for data in total_struc_data:
            df = data / data.loc['총계', :].values
            total_struc_data_per.append(df)

        return total_struc_data, total_struc_data_per

    # 연도별 특정 산업의 규모변화
    def special_industry_scale(self):

        special_industry_scale_list = []
        special_industry_scale_list_per = []

        total_industry_scale_data = self.industry_scale()[0]

        for i in self.special_industry_list:
            year = self.year
            df = pd.DataFrame(data=[], columns=[
                              '산업명', '연도', '중간수요', '최종수요', '총수요', '중간투입', '부가가치', '총투입(=총산출)', '수입계', '총공급'])
            for data in total_industry_scale_data:
                # 산업별 중간수요
                middle_demand = data.loc[i, '중간수요']
                # 산업별 최종수요
                final_demand = data.loc[i, '최종수요']
                # 산업별 총수요계
                total_demand = data.loc[i, '총수요']
                # 산업별 중간투입
                middle_input = data.loc[i, '중간투입']
                # 산업별 부가가치
                added_value = data.loc[i, '부가가치']
                # 산업별 총투입계
                total_input = data.loc[i, '총투입(=총산출)']
                # 산업별 수입계
                total_income = data.loc[i, '수입계']
                # 산업별 총공급
                total_supply = data.loc[i, '총공급']
                df.loc[len(df)] = [i, year, middle_demand, final_demand, total_demand,
                                   middle_input, added_value, total_input, total_income, total_supply]
                year += 1

            special_industry_scale_list.append(df)

        year_spac_data = pd.concat([special_industry_scale_list[i] for i in range(
            len(special_industry_scale_list))], axis=0).reset_index(drop=True)
        year_spac_data.set_index(['산업명', '연도'], inplace=True)

        # 비중
        for i in self.special_industry_list:
            year = self.year
            df = pd.DataFrame(data=[], columns=[
                              '산업명', '연도', '중간수요', '최종수요', '총수요', '중간투입', '부가가치', '총투입(=총산출)', '수입계', '총공급'])
            for data in total_industry_scale_data:
                # 산업별 중간수요
                middle_demand = data.loc[i, '중간수요'] / data.loc['총계', '중간수요']
                # 산업별 최종수요
                final_demand = data.loc[i, '최종수요'] / data.loc['총계', '최종수요']
                # 산업별 총수요계
                total_demand = data.loc[i, '총수요'] / data.loc['총계', '총수요']
                # 산업별 중간투입
                middle_input = data.loc[i, '중간투입'] / data.loc['총계', '중간투입']
                # 산업별 부가가치
                added_value = data.loc[i, '부가가치'] / data.loc['총계', '부가가치']
                # 산업별 총투입계
                total_input = data.loc[i,
                                       '총투입(=총산출)'] / data.loc['총계', '총투입(=총산출)']
                # 산업별 수입계
                total_income = data.loc[i, '수입계'] / data.loc['총계', '수입계']
                # 산업별 총공급
                total_supply = data.loc[i, '총공급'] / data.loc['총계', '총공급']
                df.loc[len(df)] = [i, year, middle_demand, final_demand, total_demand,
                                   middle_input, added_value, total_input, total_income, total_supply]
                year += 1
            special_industry_scale_list_per.append(df)

        year_spac_data_per = pd.concat([special_industry_scale_list_per[i] for i in range(
            len(special_industry_scale_list_per))], axis=0).reset_index(drop=True)
        year_spac_data_per.set_index(['산업명', '연도'], inplace=True)

        return year_spac_data, year_spac_data_per

    """
    3. 산업의 경제적 구조 및 변화 
    """
    # 1) 경제적 구조

    def economic_struc_data(self):

        industry_name = self.index_name

        total_economic_struc_data = []
        for data in self.total_data:
            df = pd.DataFrame(data=[], columns=['산업명', '중간투입률',
                              '부가가치율', '중간수요율', '최종수요율', '수출율', '수입계수'])

            df['산업명'] = industry_name
            df.set_index('산업명', inplace=True)

            for i in industry_name:
                # 산업별 중간투입률 = 중간투입 / 총투입액(=총산출액)
                middle_input_per = data.loc['중간투입계', i] / data.loc['총투입계', i]
                df.loc[i, '중간투입률'] = middle_input_per

                # 산업별 부가가치율 = 부가가치 / 총투입액(=총산출액)
                added_value_per = data.loc['부가가치계', i] / data.loc['총투입계', i]
                df.loc[i, '부가가치율'] = added_value_per

                # 산업별 중간수요율 = 중간수요 / 총수요
                middle_demand_per = data.loc[i, '중간수요계'] / data.loc[i, '총수요계']
                df.loc[i, '중간수요율'] = middle_demand_per

                # 산업별 최종수요율 = 최종수요 / 총수요
                final_demand_per = data.loc[i, '최종수요계'] / data.loc[i, '총수요계']
                df.loc[i, '최종수요율'] = final_demand_per

                # 산업별 수출율 = 수출 / 총산출액(=총투입액)
                export_per = data.loc[i, '수출'] / data.loc[i, '총산출']
                df.loc[i, '수출율'] = export_per

                # 산업별 수입계수 = 수입 / 총공급액
                # 수입인지 수입계인지 확인 요망
                total_income_per = data.loc[i, '수입계'] / data.loc[i, '총공급계']
                df.loc[i, '수입계수'] = total_income_per

            total_economic_struc_data.append(df)
        return total_economic_struc_data

    # 2) 경제적 구조의 변화(추세)

    # 특정 산업 경제적 구조의 변화
    def special_economic_struc_change(self):
        df = pd.DataFrame(data=[], columns=['산업명', '연도', '중간투입률',
                          '부가가치율', '중간수요율', '최종수요율', '수출율', '수입계수'])

        special_economic_struc_data = self.economic_struc_data()

        for i in self.special_industry_list:
            year = self.year
            for data in special_economic_struc_data:

                # 산업별 중간투입률 = 중간투입 / 총투입액(=총산출액)
                middle_input_per = data.loc[i, '중간투입률']

                # 산업별 부가가치율 = 부가가치 / 총투입액(=총산출액)
                added_value_per = data.loc[i, '부가가치율']

                # 산업별 중간수요율 = 중간수요 / 총수요
                middle_demand_per = data.loc[i, '중간수요율']

                # 산업별 최종수요율 = 최종수요 / 총수요
                final_demand_per = data.loc[i, '최종수요율']

                # 산업별 수출율 = 수출 / 총산출액(=총투입액)
                export_per = data.loc[i, '수출율']

                # 산업별 수입계수 = 수입 / 총공급액
                # 수입인지 수입계인지 확인 요망
                total_income_per = data.loc[i, '수입계수']

                df.loc[len(df)] = [i, year, middle_input_per, added_value_per,
                                   middle_demand_per, final_demand_per, export_per, total_income_per]

                year += 1
        df.set_index(['산업명', '연도'], inplace=True)
        return df

    """
    4. 산업의 경제적 효과 
    """
    # 1) 생산유발효과

    # 생산유발계수 행렬
    def input_prod_coeff(self):
        total_prod_metrix = []
        for data, domestic_data in zip(self.total_data, self.total_data_domestic):
            input_metrix = domestic_data.iloc[:, :self.metrix_num] / \
                data.loc['총투입계', :data.index.values[self.metrix_num-1]]
            input_metrix = input_metrix.iloc[:self.metrix_num,
                                             :self.metrix_num]

            prod_induc_metrix = pd.DataFrame(data=np.linalg.inv(np.identity(self.metrix_num) - input_metrix), columns=[
                                             input_metrix.columns[i] for i in range(len(input_metrix.columns))], index=[input_metrix.columns[i] for i in range(len(input_metrix.columns))])

            prod_induc_metrix['행합'] = prod_induc_metrix.sum(axis=1)
            prod_induc_metrix.loc['열합', :] = prod_induc_metrix.sum(axis=0)

            prod_induc_metrix['감응도 계수'] = prod_induc_metrix['행합'] / \
                prod_induc_metrix.loc[:data.index.values[self.metrix_num-1], '행합'].mean()
            prod_induc_metrix.loc['영향력 계수', :] = prod_induc_metrix.loc['열합', :] / \
                prod_induc_metrix.loc['열합',
                                      :data.index.values[self.metrix_num-1]].mean()

            total_prod_metrix.append(prod_induc_metrix)
        return total_prod_metrix

    # 산업별 생산유발계수
    def prod_effect_tabel(self):
        input_prod_data = self.input_prod_coeff()
        year = self.year
        df = pd.DataFrame(data=[], index=self.index_name)
        for data in input_prod_data:
            for name in self.index_name:
                df.loc[name, year] = data.loc['열합', name]
            year += 1

        return df

    # 산업별 영향력 계수 및 감응도 계수
    # 영향력 계수
    def backward_effect(self, data, index_name):
        backward_count = data.loc['영향력 계수', index_name]
        return backward_count

    # 감응도 계수
    def forward_effect(self, data, index_name):
        forward_count = data.loc[index_name, '감응도 계수']
        return forward_count

    def back_forward_table(self):
        total_prod_metrix = self.input_prod_coeff()
        year = self.year
        back_forward_name = ['영향력 계수', '감응도 계수']

        df1 = pd.DataFrame(data=[], index=self.index_name)
        for data in total_prod_metrix:
            for name in self.index_name:
                df1.loc[name, year] = self.backward_effect(data, name)
                df1.loc[name, '구분'] = '영향력 계수'
            year += 1

        year = self.year
        df2 = pd.DataFrame(data=[], index=self.index_name)
        for data in total_prod_metrix:
            for name in self.index_name:
                df2.loc[name, year] = self.forward_effect(data, name)
                df2.loc[name, '구분'] = '감응도 계수'
            year += 1

        df = pd.concat([df1, df2], axis=0)

        df['산업명'] = df.index

        df.set_index(['구분', '산업명'], inplace=True)

        return df

    # 2) 부가가치유발효과

    # 부가가치유발효과 행렬

    def added_value_coeff_metrix(self):

        total_added_value_coeff = []
        input_prod_metrix = self.input_prod_coeff()
        for i, data in enumerate(self.total_data):
            # 생산유발계수 행렬
            prod_coeff_metrix = input_prod_metrix[i].iloc[:self.metrix_num,
                                                          :self.metrix_num].values

            # 부가가치율 벡터
            added_value_per = []
            for i in self.index_name:
                added_value_per.append(
                    data.loc['부가가치계', i] / data.loc['총투입계', i])

            #  부가가치율 대각행렬
            added_value_metrix = (added_value_per * np.identity(self.metrix_num)
                                  ).reshape([self.metrix_num, self.metrix_num])

            # 부가가치유발계수행렬
            final_added_value_metrix = np.dot(
                added_value_metrix, prod_coeff_metrix)

            df = pd.DataFrame(data=final_added_value_metrix,
                              index=self.index_name, columns=self.index_name)

            df['행합'] = df.sum(axis=1)
            df.loc['열합', :] = df.sum(axis=0)
            total_added_value_coeff.append(df)
        return total_added_value_coeff

    # 산업별 부가가치유발효과

    def added_value_coeff_result(self):
        total_added_value_metrix = self.added_value_coeff_metrix()
        year = self.year
        df = pd.DataFrame(data=[], index=self.index_name)
        for data in total_added_value_metrix:
            for name in self.index_name:
                df.loc[name, year] = data.loc['열합', name]
            year += 1

        return df

    # 3) 노동유발효과
    # 산업별 총 산출액
    def total_input_prod_table(self):
        year = self.year

        df = pd.DataFrame(data=[], index=self.index_name)
        for data in self.total_data:
            for name in self.index_name:
                df.loc[name, year] = data.loc['총투입계', name]
            year += 1

        return df

    # 산업별 취업계수 및 고용계수 테이블

    def employ_coef(self):
        year = self.year
        employ_data = self.employ_data
        df = pd.DataFrame(data=[], columns=[f'취업계수_{year}', f'고용계수_{year}', f'취업계수_{year+1}', f'고용계수_{year+1}', f'취업계수_{year+2}',
                          f'고용계수_{year+2}', f'취업계수_{year+3}', f'고용계수_{year+3}', f'취업계수_{year+4}', f'고용계수_{year+4}'], index=employ_data.index)
        data = self.total_input_prod_table()
        data.loc['계', :] = data.sum(axis=0)

        for i in range(self.year, self.year+5):
            df['취업계수_{}'.format(i)] = employ_data['취업자수_{}'.format(
                i)] / data[i] * 1000
            df['고용계수_{}'.format(i)] = employ_data['피용자수_{}'.format(
                i)] / data[i] * 1000

        columns = [[f'{year}년', f'{year}년', f'{year+1}년', f'{year+1}년',  f'{year+2}년', f'{year+2}년', f'{year+3}년', f'{year+3}년', f'{year+4}년', f'{year+4}년'],
                   ['취업계수', '고용계수', '취업계수', '고용계수', '취업계수', '고용계수', '취업계수', '고용계수', '취업계수', '고용계수']]

        df2 = pd.DataFrame(data=df.values, columns=columns, index=df.index)
        # df는 취업, 고용유발계수 행렬 구할때 사용, df2 는 저장용
        return df, df2

    # 산업별 취업,고용유발계수 행렬
    def employ_coef_metrix(self):
        year = self.year
        # 생산유발계수 행렬
        total_prod_metrix = self.input_prod_coeff()

        # 취업, 노동 계수
        total_coef_table = self.employ_coef()[0]

        total_c_coef_metrix = []
        total_p_coef_metrix = []

        for metrix in total_prod_metrix:
            m = metrix.iloc[:self.metrix_num, :self.metrix_num].values

            # 취업계수
            c_coef = total_coef_table.drop('계')['취업계수_{}'.format(year)].values

            # 고용계수
            p_coef = total_coef_table.drop('계')['고용계수_{}'.format(year)].values

            # 취업유발계수 행렬
            c_coef_metrix = np.dot(c_coef * np.identity(self.metrix_num), m)

            # 고용유발계수 행렬
            p_coef_metrix = np.dot(p_coef * np.identity(self.metrix_num), m)

            df1 = pd.DataFrame(
                data=c_coef_metrix, columns=metrix.columns[:self.metrix_num], index=metrix.index[:self.metrix_num])
            df2 = pd.DataFrame(
                data=p_coef_metrix, columns=metrix.columns[:self.metrix_num], index=metrix.index[:self.metrix_num])

            df1['행합'] = df1.sum(axis=1)
            df1.loc['열합', :] = df1.sum(axis=0)

            df2['행합'] = df2.sum(axis=1)
            df2.loc['열합', :] = df2.sum(axis=0)

            total_c_coef_metrix.append(df1)
            total_p_coef_metrix.append(df2)
            year += 1
        return total_c_coef_metrix, total_p_coef_metrix

    # 노동, 고용유발계수
    def employ_coef_table(self):
        employ_coef_metrix_c = self.employ_coef_metrix()[0]
        employ_coef_metrix_p = self.employ_coef_metrix()[1]
        year = self.year
        index_names = self.index_name
        df_c = pd.DataFrame(data=[], index=index_names)
        df_p = pd.DataFrame(data=[], index=index_names)
        for data_c, data_p in zip(employ_coef_metrix_c, employ_coef_metrix_p):
            for name in index_names:
                df_c.loc[name, year] = data_c.loc['열합', name]
                df_p.loc[name, year] = data_p.loc['열합', name]
            year += 1

        return df_c, df_p

    # 산업별 취업 및 고용유발효과
    def total_employ_coef_table(self):
        total_c_table = self.employ_coef_table()[0]
        total_p_table = self.employ_coef_table()[1]

        df = pd.concat([total_c_table, total_p_table], axis=1)

        year_name = list(df.columns)

        multi = ['취업유발계수', '취업유발계수', '취업유발계수', '취업유발계수', '취업유발계수',
                 '고용유발계수', '고용유발계수', '고용유발계수', '고용유발계수', '고용유발계수']

        multi_column = [multi, year_name]

        concat_df = pd.DataFrame(
            data=df.values, columns=multi_column, index=df.index)

        return concat_df
