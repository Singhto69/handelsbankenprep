import re

import pandas as pd


class PandasTutorial():
    def __init__(self):
        self.dummy = 0

    def tutorial001(self):
        mydataset = {
            'cars': ["BMW", "Volvo", "Ford"],
            'passings': [3, 7, 2]
        }
        myvar = pd.DataFrame(mydataset)
        return (myvar)

    def tutorial002(self):
        a = [1, 7, 2]
        myvar = pd.Series(a, index=["x", "y", "z"])
        return myvar['x']

    def tutorial003(self):
        calories = {"day1": 420, "day2": 380, "day3": 390}
        return pd.Series(calories)

    def tutorial004(self):
        calories = {"day1": 420, "day2": 380, "day3": 390}
        return pd.Series(calories, index=["day1", "day2"])

    def tutorial005(self):
        data = {
            "calories": [420, 380, 390],
            "duration": [50, 40, 45],
            "fat content(g)": [30, 12, 18]
        }
        df = pd.DataFrame(data, index=["Mcdonalds", "chicken", "broccolisoup with butter"])
        return df.loc[["Mcdonalds", "chicken"]]
        # Why the need for a subarray for index lookups with loc??

    def tutorial006(self):
        data = {
            "Duration": {
                "0": 60,
                "1": 60,
                "2": 60,
                "3": 45,
                "4": 45,
                "5": 60
            },
            "Pulse": {
                "0": 110,
                "1": 117,
                "2": 103,
                "3": 109,
                "4": 117,
                "5": 102
            },
            "Maxpulse": {
                "0": 130,
                "1": 145,
                "2": 135,
                "3": 175,
                "4": 148,
                "5": 127
            },
            "Calories": {
                "0": 409,
                "1": 479,
                "2": 340,
                "3": 282,
                "4": 406,
                "5": 300
            }
        }
        df = pd.DataFrame(data)
        return df

    def tutorial007(self):
        # print(pd.options.display.max_rows)
        pd.options.display.max_rows = 9999
        df = pd.read_csv(filepath_or_buffer='tutorials/data.csv')
        # js = df.to_dict()
        # js["Pulse"]
        # df.head(10)
        # df.tail(10)
        # df.info()
        return df.info()

    def tutorial008(self):
        df = pd.read_csv(filepath_or_buffer='tutorials/data.csv')
        # df.dropna(inplace=True)
        meanval = int(df["Calories"].mean())
        # median = df["Calories"].median()
        mode = df["Calories"].mode()[0]  # Mode = most common ocurring val
        df.fillna(value={"Calories": meanval}, inplace=True)
        # df.loc[3, 'Duration'] = 60
        # df.index = RangeIndex(start=0, stop=169, step=1)
        for i in df.index:
            if df.loc[i, 'Duration'] > 60:
                df.loc[i, 'Duration'] = 60
                # df.drop(i,inplace=True)

        return df.duplicated()
        # df.drop_duplicates(inplace = True)
        # return df.head(32).to_string()

    def problem595(self):
        data = [['Afghanistan', 'Asia', 652230, 25500100, 20343000000],
                ['Albania', 'Europe', 28748, 2831741, 12960000000],
                ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000],
                ['Angola', 'Africa', 1246700, 20609294, 100990000000]]
        world = pd.DataFrame(data, columns=['name', 'continent', 'area', 'population', 'gdp']).astype(
            {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})
        # print(world.to_string())
        # for i in world.index:
        #    if world.loc[i, 'area'] < 3000000 and world.loc[i, 'population'] < 25000000:
        #        world.drop(i, inplace=True)

        # world = world.drop(columns=["continent", "gdp"])
        # return world.loc[(world['population'] >= 25000000) | (world['area'] >= 3000000), ['name', 'population', 'area']]
        return world.loc[(world['area'] >= 3000000) | (world['population'] >= 25000000), ["name", "area", "population"]]

    def problem1757(self):
        data = [['0', 'Y', 'N'], ['1', 'Y', 'Y'], ['2', 'N', 'Y'], ['3', 'Y', 'Y'], ['4', 'N', 'N']]
        products = pd.DataFrame(data, columns=['product_id', 'low_fats', 'recyclable']).astype(
            {'product_id': 'int64', 'low_fats': 'category', 'recyclable': 'category'})
        filter = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
        return products.loc[filter, ["product_id"]]
        # return products.product_id[filter].to_frame()

    def problem183(self):
        data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
        customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
        data = [[1, 3], [2, 1]]
        orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
        return (
            customers[~customers['id'].isin(orders['customerId'])].drop(columns='id').rename(
                columns={'name': 'Customers'})
        )
        # return pd.merge(customers, orders, left_on='id', right_on='id')

    def problem1148(self):
        data = [[1, 3, 5, '2019-08-01'], [1, 3, 6, '2019-08-02'], [2, 7, 7, '2019-08-01'], [2, 7, 6, '2019-08-02'],
                [4, 7, 1, '2019-07-22'], [3, 4, 4, '2019-07-21'], [3, 4, 4, '2019-07-21']]
        views = pd.DataFrame(data, columns=['article_id', 'author_id', 'viewer_id', 'view_date']).astype(
            {'article_id': 'Int64', 'author_id': 'Int64', 'viewer_id': 'Int64', 'view_date': 'datetime64[ns]'})
        return (views[views['author_id'] == views['viewer_id']]['author_id']
                .reset_index(drop=True)
                .drop_duplicates()
                .to_frame().rename(columns={'author_id': 'id'})
                .sort_values(by='id', ascending=True))

    def problem1683(self):
        data = [[1, 'Vote for Biden'], [2, 'Let us make America great again!']]
        tweets = pd.DataFrame(data, columns=['tweet_id', 'content']).astype({'tweet_id': 'Int64', 'content': 'object'})
        return (tweets[tweets['content']
                .str.len() > 15]['tweet_id']
                .reset_index(drop=True)
                .to_frame())

    def problem1873(self):
        data = [[2, 'Meir', 3000], [3, 'Michael', 3800], [7, 'Addilyn', 7400], [8, 'Juan', 6100], [9, 'Kannon', 7700]]
        employees = pd.DataFrame(data, columns=['employee_id', 'name', 'salary']).astype(
            {'employee_id': 'int64', 'name': 'object', 'salary': 'int64'})
        condA = employees['employee_id'] % 2 == 0
        condB = employees['name'].str.startswith('M')
        employees.loc[condA | condB, 'salary'] = 0
        return (employees[['employee_id', 'salary']]
                .rename(columns={'salary': 'bonus'})
                .sort_values(by='employee_id', ascending=True))

    def problem1667(self):
        data = [[1, 'aLice'], [2, 'bOB']]
        users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id': 'Int64', 'name': 'object'})
        users['name'] = users['name'].str.capitalize()
        return users.sort_values(by='user_id', ascending=True)

    def problem1517(self):
        data = [[1, 'Winston', 'winston@leetcode.com'], [2, 'Jonathan', 'jonathanisgreat'],
                [3, 'Annabelle', 'bella-1@leetcode.com'], [4, 'Sally', 'sally.come@leetcode.com'],
                [5, 'Marwan', 'quarz#2020@leetcode.com'], [6, 'David', 'david69@gmail.com'],
                [7, 'Shapiro', '.shapo@leetcode.com']]
        users = pd.DataFrame(data, columns=['user_id', 'name', 'mail']).astype(
            {'user_id': 'int64', 'name': 'object', 'mail': 'object'})

        s = "B@leetcode.com"
        pattern = r'^[a-zA-Z][a-zA-Z0-9\.\-_]*@leetcode\.com$'
        condition = users['mail'].str.match(pattern)
        # return re.fullmatch(pattern, s)
        # users = users.where(users['mail'].str.match(pattern, na=False)).dropna()
        # users['user_id'] = users['user_id'].astype(int)
        # return users
        return users[condition]

    def problem1527(self):
        data = [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'],
                [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']]
        patients = pd.DataFrame(data, columns=['patient_id', 'patient_name', 'conditions']).astype(
            {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})
        # pattern = r'^{7}$'
        pattern = r'\bDIAB1'
        condition = patients['conditions'].str.contains(pattern)
        return patients[condition]

    def problem196(self):
        data = [[1, 'john@example.com'], [2, 'bob@example.com'], [3, 'john@example.com']]
        # Leetcode submission edition
        # person.sort_values(by='id', ascending=True, inplace=True)
        # person.drop_duplicates(subset='email', keep='first', inplace=True)
        person = pd.DataFrame(data, columns=['id', 'email']).astype({'id': 'int64', 'email': 'object'})
        return person.sort_values(by='id', ascending=True).drop_duplicates(subset='email', keep='first')

    def problem1795(self):
        data = [[0, 95, 100, 105], [1, 70, None, 80]]
        products = pd.DataFrame(data, columns=['product_id', 'store1', 'store2', 'store3']).astype(
            {'product_id': 'Int64', 'store1': 'Int64', 'store2': 'Int64', 'store3': 'Int64'})
        # products = products.pivot_table(index='product_id', columns='store', values='price')
        products = (pd.melt(frame=products, id_vars='product_id', var_name='store', value_name='price')
                    .dropna()
                    .sort_values(by='product_id', ascending=True)
                    )
        return products

    def problem177(self):
        data = [[1, 100], [2, 200], [3, 300]]
        employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'Int64', 'salary': 'Int64'})
        N = -1

        employee = employee.drop_duplicates(subset='salary')
        if N <= len(employee.index) and N > 0:
            nth_highest_salary = employee['salary'].nlargest(N).iloc[-1]
            f = pd.DataFrame([nth_highest_salary], columns=[f"getNthHighestSalary({N})"]).astype(
                {f"getNthHighestSalary({N})": 'Int64'})
            return f
        else:
            f = pd.DataFrame([None], columns=['getNthHighestSalary(' + str(N) + ')'])
            return f

    def problem176(self):
        data = [[1, 100], [2, 200], [3, 300]]
        employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'int64', 'salary': 'int64'})

        employee = employee.drop_duplicates(subset='salary')
        if len(employee.index) > 1:
            nth_highest_salary = employee['salary'].nlargest(2).iloc[-1]
            f = pd.DataFrame([nth_highest_salary], columns=['SecondHighestSalary']).astype(
                {'SecondHighestSalary': 'Int64'})
            return f
        else:
            f = pd.DataFrame([None], columns=['SecondHighestSalary'])
            return f

    def problem184(self):
        data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2],
                [5, 'Max', 90000, 1]]
        employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
            {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
        data = [[1, 'IT'], [2, 'Sales']]
        department = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
        employee = employee.sort_values(by='departmentId', ascending=True)
        # employee.iloc[0].departmentId, employee.iloc[-1].departmentId
        # for i in range(0, employee['departmentId'].nunique()):
        employee = employee.groupby(by=['departmentId'])
        return employee
