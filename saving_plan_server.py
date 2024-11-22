from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == "POST":



        #Input Handling
        data = request.form['input'] 
        d = data.split(",")
        w = int(d[0])
        d1 = ""
        d2 = ""
        for el in d[1]:
            if el not in['[',']']:
                d1 = d1+el
        for el in d[2]:
            if el not in['[',']']:
                d2 = d2+el  
        vv = d1.split(" ")
        wtt = d2.split(" ")
        val = []
        wt = []
        for i in range(len(vv)):
            val.append(int(vv[i]))
            wt.append(int(wtt[i]))



        #Saving Print Variables    
        p_w = w
        p_val = val
        p_wt = wt
        n = len(val)



        #Dp Code For 0/1 Knapsack
        def zo_knapsack(n,w,val,wt):
            dp = [[0 for i in range(w+1)] for j in range(n+1)]
            #initialization done already
            for i in range(1,n+1):
                for j in range(1,w+1):
                    if wt[i-1] <= j:
                        dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],dp[i-1][j])
                    else:
                        dp[i][j] = dp[i-1][j]    
            return dp
        dp = zo_knapsack(n,w,val,wt)
        result = dp[n][w]




        #Back iterating table we got from 0/1 Knapsack
        l = []
        for i in range(n,0,-1):
            if result == 0:
                break

            if result == dp[i-1][w]:
                continue

            else:
                l.append(i-1)
                result = result - val[i-1]
                w = w - wt[i-1]
        


        #Output Formatting
        s = "You Should Buy Items " +str(sorted(list(map(lambda x:x+1,l))))
        cost = " At Cost "
        c = 0 
        for i in range(0,len(l)): 
            c += wt[l[i]]
        cost = " at Cost " + str(c) 
        s = s + cost + " for the case         " + "Budget = " + str(p_w) + "  Index " + str([i for i in range(1,len(p_val)+1)]) + "  Priority = " + str(p_val) + "  Cost = " + str(p_wt)
        return redirect(url_for('output',v = s))
    else:
        return render_template("saving_plan.html")         

@app.route("/output/<v>")
def output(v):
    return render_template("output.html",val = v) 


if __name__ == "__main__":
    app.run()   
