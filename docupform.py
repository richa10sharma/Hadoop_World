#!/usr/bin/python
import cgi,commands,os
#print "Set-Cookie:NIP=192.168.43.102;\n"
#print "Set-Cookie:JIP=192.4168.43.196;\r\n"
#print "Set-Cookie:Path=/l.py;\n"
print "Content-type:text/html\n"
print """
<!doctype html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Hadoop</title>
        <style>
	body{
    background: #f0f2f3;
    overflow-x: hidden;
    margin: 0;
    padding: 0;
    border: 0;
   
}
#header{
    background: rgba(255,255,255,0.8);
    height: 80px;
    position: fixed;
    float: left;
    width: 110%;
    overflow: hidden;
    margin-left: -10px;
    border: 0;
    top:0;
    z-index: 500;
    box-shadow: 0px 4px 16px #949494;
   
}
.downe{
    height: 40px;
    width: 40px;
    position: absolute;
    right: 20px;
    top: 100px;
    opacity: 0.4;
    transition: opacity 0.3s ease-in-out; 
}
.downe:hover{
    opacity: 1;
}
#cb{
    font-size: 45px; /* use font-size 38px with source sans pro   */
    padding-right: 100px;
    font-family: bombing,Source Sans Pro,Roboto;
    font-weight: 300;
    -webkit-box-reflect:below -20px -webkit-gradient(linear,left top, left bottom,from(transparent),color-stop(0.56,transparent), to(rgba(255,255,255,0.8)));
    transition: transform 0.2s ease-in-out; 

    
    
}

#cb:hover{
    transform: translate(-10px,0px);
     transform: translate(20px,0px);
}
#intro{
    font:20px Source Sans Pro;
    width:700px;
    text-align: center;
    margin: 150px auto;
    position:relative;
    z-index: :-1;
    font-weight: 300;
    
}

#download{
    z-index: 1;
    width: 240px;
    height: 50px;
    position: relative;
    overflow: hidden;
    background: #2745de;
    color: #2be3f3;
    font: 25px Candara;
    margin: -70px auto;
    text-align: center;
    padding: 10px;
    border:4px solid #2be3f3;
    transition: background 1.5s ease-out, color 1.1s ease-out, box-shadow 0.4s ease-in, border-top-left-radius 0.6s ease-out,border-bottom-right-radius 0.6s ease-out;

} 
#download:hover{
    background: #051b89;
    color: white;
    box-shadow: 0px 0px 18px #000000;
    cursor: pointer;
    border-top-left-radius: 50px;
    border-bottom-right-radius: 50px;
     
}
ul{
    list-style: :none;
}
li{
    display: inline-block;
    padding-right: 70px;
    border: :none;
    font: 20px Diavlo Light,Tahoma,Verdana,sans-serif;
    font-weight: light;
}
th{
    font: 30px Source Sans Pro;
    font-weight: 300;
}
td{
    font: 19px Candara;
    width: 600px;
    padding: 12px 40px 10px 20px;
}
#td2{
    padding-top: 0px;
    border-left:1px solid white;
}
#midsection{
    background: #f9f8fa;
    transition: -webkit-linear-gradient 1.5s ease-in-out,color 0.6s ease-in-out;

    
}

#midsection p{
    font:30px Roboto;
    font-weight: 200;
    margin: auto;
    width: 850px;
    padding-top: 15px;
    padding-bottom: 15px;
}
#midsection:hover{
color: white;
  background: -webkit-linear-gradient(#648880, #293f50);
}
#tweet{
    right: 150px;
}
img{
    width: 40px;
    height: 40px;
    position: absolute;
    right:25px;
    top:25px;
    
   
}
#fbt{
    width: 55px;
    height: 55px;
    position: absolute;
    right:220px;
    top:20px;
}
#home{
    height: 35px;
    width: 35px;
    left: 270px;
    top: 25px;
    position: absolute;
    opacity: 0.4;
}
#home:hover{
    opacity: 1;
}
li a{
    text-decoration: none;
    color:darkgrey;
}
li a:hover{
    color: black;
}
#sidebar{
    background: black;
    top: 160px;
    float: left;
    width:200px;
    overflow-y: scroll;
    z-index: 1;
    height: 310px;
    left: 0;
    position: absolute;
    box-shadow: 5px 0px 15px darkgrey ;
    overflow-x: hidden;
}
#tutorials{
    margin: 0;
    padding: 0;
}
#tutorials li{
    display: block;
    color: #ababab;
    font: 18px Candara;
    padding: 10px;
    width: 200px;
    margin: 0;
    border: 0;
   left: 0px;
    position: relative;
    text-align: center;
    transition: transform 0.4s ease, background 0.3s ease-in, color 0.2s ease;
}
#tutorials li:hover{
    color: white;
    cursor: pointer;
    transform: translate(-10px,0px);
  
}
#tutorials li:first-child {
    color: crimson;
    text-align: center;
    font: 18px Verdana;
    left:0px;
}
    
}
body::-webkit-scrollbar {
    width: 15px;
    
}
 
body::-webkit-scrollbar-track {
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3); 
    border-radius: 10px;
}
 
body::-webkit-scrollbar-thumb {
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.5); 
    scrollbar-base-color: black;
}
#sidebar::-webkit-scrollbar{
    width: 7px;
}
#sidebar::-webkit-scrollbar-thumb {
    background: #535353;
    width: 7px;
    border-radius: 0px;
}
#sidebar::-webkit-scrollbar-track, -wbkit-scrollbar-thumb:hover -webkit-scrollbar-thumb{
    background: #629c87;
}
#sidebar::-webkit-scrollbar-track{
    background: rgba(0,0,0,0.7);
    -webkit-box-shadow: inset 0 0 4px rgba(0,0,0,0.3);
    
}
#footer{
    width: 200%;
    height: 300px;
    bottom: 0;
    background: black;
    float: left;
    position: relative;
    z-index: -2;
    margin-bottom: 0;
    left: 0;
    padding: 0;
    border: 0;
    margin-left: -10px;
    overflow-x: hidden;
    border-top: 10px solid #e831f3;
    -webkit-animation-name: borderchange;
    -webkit-animation-duration: 2s;
    -webkit-animation-iteration-count: infinite;
    animation-name: borderchange;
    animation-duration: 2s;
    animation-iteration-count: infinite;
    animation-direction: alternate;
    
}
@-webkit-keyframes borderchange{
    0% {border-top: 10px solid #e831f3;}
    50% {border-top: 10px solid #28f12c;}
    100% {border-top: 10px solid #27e7ee;}
}
#footer td{
    position: relative;
    margin-left: 25px;
    margin-top: 40px;
    padding: 0px;
    border: 0;
    height: auto;
    margin: 0;
}
#footer table{
        margin-left: 25px;
    margin-top: 28px;
}

#footer tr{
    padding: 0;
    height: 20px;
    margin-left: 25px;
    margin-top: 28px;
    margin-bottom: 0;
    position: relative;
} 
#footer td a{
    text-decoration: none;
    padding: 0;
    margin: 0;
    border: 0;
    color: #049acb;
    font-size: 15px;
}
td a: nth-child(1){
    color: white;
    z-index: 4;
}

#download span{
    display: block;
    position: absolute;
    padding: 0;
}
#top{
    color: #27f3f5;
    top: 2px;
    transition: top 0.6s, opacity 0.8s;
    opacity: 1;
}
#bottom{
    top: 70px;
    left: 50px;
    font: 32px Source Sans Pro;
    font-weight: bold;
    transition: top 0.6s, opacity 0.8s;
    opacity: 0.4;
    
}
#download:hover #top{
    top:  -65px;
    opacity: 0;
}
#download:hover #bottom{
    top: 12px;
    opacity: 1;
}
#imgdiv{
    height: 350px;
    width: 300px;
    margin-left: 100px;
    position: relative;
    background: #ffffff;
    -webkit-align-content: center;
    align-content: center;
    box-shadow: 4px 10px 15px #949494;
    padding-bottom: 10px;
    display: block;
     transition: transform 0.3s ease,background 0.4s, color 0.3s;
}
#imgdiv img{
    position: absolute;
    top: 0;
    left: 0;
    padding: 0;
    margin: 0;
    border: 0;
    width: 300px;
    height:280px;
}
#imgdiv p{
    position: absolute;
    top: 285px;
    left: 0px;
    width: 300px;
    padding: 0;
    margin: 0;
    border: 0;
    text-align: center;
    font: 18px Source Sans Pro;
    
}
#imgdiv2{
    height: 350px;
    width: 300px;
    margin-left: 500px;
    position: relative;
    background: #ffffff;
    -webkit-align-content: center;
    align-content: center;
    box-shadow: 4px 10px 15px #949494;
    padding-bottom: 10px;    
    display: block;
    margin-top: -360px;
   transition: transform 0.3s ease,background 0.4s, color 0.3s;
}
#imgdiv2 img{
    position: absolute;
    top: 0;
    left: 0;
    padding: 0;
    margin: 0;
    border: 0;
    width: 300px;
    height:280px;    
}
#imgdiv2 p{
    position: absolute;
    top: 285px;
    left: 0px;
    width: 300px;
    padding: 0;
    margin: 0;
    border: 0;
    text-align: center;
    font: 18px Source Sans Pro;    
}
#imgdiv3{
    height: 350px;
    width: 300px;
    margin-left: 900px;
    position: relative;
    background: #ffffff;
    -webkit-align-content: center;
    align-content: center;
    box-shadow: 4px 10px 15px #949494;
    padding-bottom: 10px;    
    display: block;
    margin-top: -360px;
   transition: transform 0.3s ease,background 0.4s, color 0.3s;
}
#imgdiv3 img{
    position: absolute;
    top: 0;
    left: 0;
    padding: 0;
    margin: 0;
    border: 0;
    width: 300px;
    height:280px;    
}
#imgdiv3 p{
    position: absolute;
    top: 285px;
    left: 0px;
    width: 300px;
    padding: 0;
    margin: 0;
    border: 0;
    text-align: center;
    font: 18px Source Sans Pro;    
}
#imgdiv:hover{
    background: #23c6e3;
    color: white;
    transform: translate(0px -4px);    
}
#imgdiv2:hover{
    background: #23c6e3;
    color: white;
    transform: translate(0px -4px);    
}
#imgdiv3:hover{
    background: #23c6e3;
    color: white;
    transform: translate(0px -4px);
}
.imgdivs:hover{
    cursor: pointer;
}

	</style>
        <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400' rel='stylesheet' type='text/css'>
        
    </head>
    <body>
        <div id="header">
            <ul>
                
                <li id="cb">Hadoop</li>

                <li><a href="firstpage.py"><img id="home" src="homee.png" /></a></li>

                <li href="#"><a href="form.py">ManualSetUp</a></li>

                <li href="#"><a href="autoform.py">AutomaticSetUp</a></li>

                <li href="#"><a href="dockerform.py">OnDemandSetUp</a></li>

		<li href="#"><a href="#">Contact</a></li>
                <li><a title="Twitter" href="https://www.google.co.in/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwjI7q-s6c_NAhUlSY8KHaZLC_YQFggmMAA&url=https%3A%2F%2Ftwitter.com%2F%3Flang%3Den&usg=AFQjCNEC1-VaUkNHL90ZFoJUbNqV_YWc6w" target="_blank"><img id="tweet" src="tweety2.png" /></a></li>
                <li><a title="Facebook" href="https://www.facebook.com/" target="_blank"><img id="fbt" src="fbt.png" /></a></li>
            
            </ul>
            
        </div>
        <a id="downd" href="#footer"><img  title="Down" class="downe" src="arrow-down.png" /></a>
        
   <div id="intro">

"""
	

print """

<form align ="right" action="http://192.168.43.102/cgi-bin/updoc.py" method="post">
<br>You can upload your file to HDFS<br><br><br>
FILE NAME : <input name='nfile'  type='text' /><br>
		<br><br>
		<input type='submit' />
	</form>



"""
print """

</div>
               
        <hr style="border-color:#d9d9d9;border-width:0.089px">
        <br><br>
        <div id="sidebar">
            <ul id="tutorials">
                <li id="CBT">Quick Links</li><br>

                <li><a href="docjobf.py">AssignJob</a></li>

                <li><a href="docclustercheck.py">ViewClusterStatus</a></li>

                <li><a href="docupform.py">UploadFile</a></li>

		<li><a href="#">CheckASystem</a></li>

		<li><a href="hdfs.py">ViewHDFS</a></li>

            </ul>
            

        </div>
        
        <br><br><br><br><br><br>
        <div id="footer">
            <table>
                <tr><td><a id="ql" href="#">Quick Links</a></td></tr>
                <tr><td><a href="#">Home</a></td></tr>
                <tr><td><a href="#">APIs</a></td></tr>
                <tr><td><a href="#">Blog</a></td></tr>
                <tr><td><a href="#">Contact</a></td></tr>
                <tr><td><a href="#">Support</a></td></tr>
                <tr><td><a  href="#header">TOP</a></td></tr>
            
            </table>
        
        </div>
    </body>

</html>
"""
