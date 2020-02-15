gaana="""Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, ..
Aankh Mare O Ladka Aankh Mare
Aankh Mare O Ladka Aankh Mare
Sitti Bajaye, Sataye
Sitti Bajaye, Bich Sadak Pe
Hi Naam Mera Pukare Oh Karke Isare
O Ladka Aankha Mare
Aankh Mare O Ladki Aankh Mare
Aankh Mare O Ladki Aankh Mare
Dil Dhadkaye Pataye
Dil Dhadkaye, Bich Sadak Mein Nakhare Dikhaye Sare
Ho Karke Isare
Vo Ladki Aankh Mare
Aankh Mare Vo Ladka Aankha Mare
Aankh Mare Vo Ladki Aankha Mare
Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, Hi Ho Ha..
Are Aage Aage Bhagu Main Ye
Pichhe Pichhe Aaye
Kuchh Na Dekhe Kuchh Na Soche
Aankhe Miche Aaye, Haye Maja Aa Jaye
Ye Gadi Ke Niche Aa Jaye
P P Pagal S S S Sadayi Di Di Deewana
Tu Ye To Bata Main Kiska Deewana
Sun Le Jara Ye Sara Jamana
Dil Dhadkaye Pataye
Dil Dhadkaye Bich Sadak Mein Nakhare Dikhaye Sare
Ho Karke Isare
Vo Ladki Aankh Mare
Aankh Mare Vo Ladka Aankha Mare
Aankh Mare Vo Ladki Aankha Mare
Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, ..
Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, ..
Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, ..
Main Important Aashiq Hu But
You My Love Kya Jaane
London Se Amrika Tak Mere Kitne Deewane
I Come India For You Darling
Tu Maane Ya Na Maane
D D Dear Me Me Mear No F F Fear
Go Back U He Tu Angreja Babu Aisa Kya
Ha Mujhpe Chalega Na Tera Jaadu
Sitti Bajaye, Sataye
Sitti Bajaye, Bich Sadak Mein
Hai Naam Mera Pukare Oh Karke Isare
Wo Ladka Aankha Mare
Aankh Mare O Ladki Aankh Mare
Aankh Mare O Ladki Aankh Mare
Dil Dhadkaye Pataye
Dil Dhadkaye Bich Sadak Mein Nakhare Dikhaye Sare
Ho Karke Isare
Vo Ladki Aankh Mare
Aankh Mare Vo Ladka Aankha Mare
Aankh Mare Vo Ladki Aankha Mare
Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, ..
Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, ..
Hi Ho Ha, Hi Ho Ha, Hi Ho Ha, .."""
lyrics=gaana.split()

D={}

for i in lyrics:
                if i in D:
                                D[i]+=1
                else:
                                D[i]=1
max_value=max(D.values())

for i in D:
                if D[i]==max_value:
                                result=i
                                break
print(result)


