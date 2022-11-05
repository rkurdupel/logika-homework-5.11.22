import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')

# Очищення даних із першого завдання
# Заміни тип даних на дробове число (float) для цін додатків (Price)
# print(df["Price"].mean())

print(df["Installs"])

def remove_sign(word):
    if word[0] == "$":
        print(word[1:])
        return float(word[1:])
    
    elif word[-1] == "+":
        replace = word.replace(",", "") # replace() - замінити певну букву /  символ на іншу букву / символ
        #print(replace)
        print(replace[:-1])
        #print(type(replace[:-1]))
        return float(replace[:-1])


df["Price"] = df["Price"].apply(remove_sign)    # apply - застосувати певну функцію до рядка
df["Installs"] = df["Installs"].apply(remove_sign)


print(df.info())


#print(type(df["Price"]))
#print(df["Price"].mean())


# Обчисли, скільки доларів розробники заробили на кожному платному додатку
df["Profit"] = df["Installs"] * df["Price"]

print(df["Profit"])
# Чому дорівнює максимальний дохід ('Profit') серед платних додатків (Type == 'Paid')?
paid = df[df["Type"] == "Paid"]
print(df[df["Type"] == "Paid"]["Profit"].max())

# Створи новий стовпець, у якому зберігатиметься кількість жанрів. Назви його 'Number of genres'
print(df["Genres"])


def count_genres(genres):
    genres = genres.split(";")  # split() - розділяє слово за певним символом на частини і виводе як список
    return len(genres)  # len() - довжина слова, списка, словника, кортежу

df["Number of Genres"] = df["Genres"].apply(count_genres)

print(df["Number of Genres"])
# Яка максимальна кількість жанрів (Number of genres) зберігається в датасеті?
print(df["Number of Genres"].max()) # max() - вивести максимальну кількість значень

# Бонусне завдання
# Створи новий стовпець, що зберігає сезон, в якому було зроблено останнє оновлення (Last Updated) програми. Назви його 'Season'

# def count_season_update(season):
#     winter = []
#     # if "January" in season:
#     # winter += 1
#     all_months = ["December", "January", "February"]
#     print(season)
#     if "December" in season:
#         for all_months[0] in season:
#             winter.append(7)
#     print(len(winter))

#count_season_update(df["Last Updated"])

a = 0
s = 0
summer = 0
autumn = 0

def last_update(data):
    data = data.split(",")
    
    #return data[1]
    if "December" in data[0] or "January" in data[0] or "February" in data[0]:
        print(34)
        global a
        a += 1
    
    if "March" in data[0] or "April" in data[0] or "May" in data[0]:
        print(78)
        global s 
        s += 1
    
    if "June" in data[0] or "July" in data[0] or "August" in data[0]:   # data[0] перша частина / елемент
        print(96757)
        global summer
        summer = summer + 1
    
    if "September" in data[0] or "October" in data[0] or "November" in data[0]:
        print(79969)
        global autumn
        autumn = autumn + 1

    return f"Winter {a},Spring {s},Summer {summer},Autumn   {autumn}"

       

print(df["Last Updated"])
df["Season"] = df["Last Updated"].apply(last_update)
print(df["Season"])
# Виведи на екран сезони та їх кількість у датасеті
