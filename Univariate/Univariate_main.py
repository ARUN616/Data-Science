class Univariate_variable():
    def Univariate(data):
        Quan=[]
        Qual=[]
        for column_name in data.columns:
            if data[column_name].dtypes=='O':
                Qual.append(column_name)
            else:
                Quan.append(column_name)

        return Quan,Qual