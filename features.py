from flask import Flask

FAI=Flask(__name__)

@FAI.route('/firststringresponse')
def firststringresponse():
    return '<center><h1 style="color: brown;">Here is the first response from Flask Project</h1></center>'

if __name__=='__main__':
    FAI.run(debug=True)
