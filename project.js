var express = require('express'); 
var app = express(); 
var path = require('path');
var bodyParser = require('body-parser');

var urlencodedParser = bodyParser.urlencoded( {extend: false } )




var sys = require('sys');
var exec = require('child_process').exec;
function puts(error, stdout, stderr) {
    sys.puts(stdout);
}

app.set('views','./views');
app.set('view engine','ejs');



app.use(express.static(path.join(__dirname, 'public')));
app.use(express.static('files'));
app.use('/static', express.static('public'));

app.post('/realtime', urlencodedParser, function(req, res)  {
 	if ( req.body.realtime == 'on' ) {
 	   // service motion start
           exec("service motion start",puts);
           //res.send('start service' );
	     res.render('start');
	
	
        }
	else { 
           // service motion stop
           exec("service motion stop",puts);
	   //res.send('stop service');
	     res.render('stop');

        }
});


app.post('/sensor', urlencodedParser, function(req, res)  {
        if ( req.body.sensor == 'on' ) {
           // service motion start
           exec("python  /home/pi/pirtest.py",puts);
           //res.send('start' );
	     res.render('start'); 
       }
        else {
           // service motion stop
           exec("SIGINT /home/pi/pirtest.py",puts);
           //res.send('stop');
	     res.render('stop');
        }
});



//app.get('/', function (req, res) {
//  res.send('<html><title>Home</title><meta name="viewport" content="width=device-width, initial-scale=1"><link rel="stylesheet" href="http://www.w3schools.com/lib/w3.css"><link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Raleway"><link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css"><style>body,h1,h2,h3,h4,h5,h6 {font-family: "Raleway", sans-serif}body, html {height: 100%;line-height: 1.8;}.bgimg-1 {background-position: center;background-size: cover;background-image: url("/w3images/tablet_pen.jpg");min-height: 100%;}.w3-navbar li a {padding: 16px;float: left;}</style><body><!-- Navbar (sit on top) --><div class="w3-top"><ul class="w3-navbar" id="myNavbar"><!-- Float links to the right --><li class="w3-right w3-hide-small"><a href="control.html">Project Control</a><a href="/../video/videopage.html">Video</a><a href="picturepage.html">Picture</a><a href="http://192.168.137.236:8081/">Realtime</a></li><!-- Hide right-floated links on small screens and replace them with a menu icon --><li><a href="javascript:void(0)" class="w3-right w3-hide-large w3-hide-medium" onclick="w3_open()"><i class="fa fa-bars w3-padding-right w3-padding-left"></i></a></li></ul></div><nav class="w3-sidenav w3-black w3-card-2 w3-animate-left w3-hide-medium w3-hide-large" style="display:none" id="mySidenav"><a href="javascript:void(0)" onclick="w3_close()" class="w3-large w3-padding-16">Close ×</a><a href="control.html">Project Control</a><a href="/../video/videopage.html">Video</a><a href="picturepage.html">Picture</a><a href="http://192.168.137.236:8081/">Realtime</a></nav><!-- Header with full-height image --><header class="bgimg-1 w3-display-container w3-grayscale-min" id="home"><div class="w3-display-left w3-padding-xxlarge w3-text-black"><span class="w3-jumbo w3-hide-small">Antitheft-Project</span><br><p><a href="/../video/videopage.html" class="w3-btn w3-padding-large w3-large">Video</a></p><br><p><a href="picturepage.html" class="w3-btn w3-padding-large w3-large">Picture</a></p></div></header></body><br><footer class="w3-center w3-black w3-padding-64"><div class="w3-xlarge"><a href="#" class="w3-hover-text-indigo"><i class="fa fa-facebook-official"></i></a><a href="#" class="w3-hover-text-red"><i class="fa fa-pinterest-p"></i></a><a href="#" class="w3-hover-text-light-blue"><i class="fa fa-twitter"></i></a><a href="#" class="w3-hover-text-grey"><i class="fa fa-flickr"></i></a><a href="#" class="w3-hover-text-indigo"><i class="fa fa-linkedin"></i></a><a href="#home" class="w3-hover-text-red" title="Go to top"><i class="fa fa-arrow-up"></i></a></div><p>Powered by <a href="http://www.w3schools.com/w3css/default.asp" title="W3.CSS" target="_blank" class="w3-hover-text-green">group</a></p></footer></html>');
//});

app.get('/', function (req, res) {
   res.render('home');
});

app.listen(8000, function () {
  console.log('Example app listening on port 8000!');
});

