//sets counter to 0
let counter = 0;

function setup() {
//Canvas size 1280 by 899
  createCanvas(1280,899);
//Alert create to dispaly instrutions
  var start = alert ("Use the mouse to control the white box. Guide the red box to the green goal and win. To move on to the next level scroll down after winning. If you get stuck in a corner its best to just refresh the page.");
//used to create the objective
  boxes = createSprite(random(80, 100), random(100, 200),25, 25);
  boxes.shapeColor = color(255, 0, 0);
//used to create the player
  player = createSprite(100, 100, 40, 40);
  player.shapeColor = color(255);
//used to create the end
  win = createSprite(random(1200, 1200), random(500, height-200),25, 25);
  win.shapeColor = color(0,255,0);
  win1 = createSprite(1233,845,25, 25);
  win1.shapeColor = color(40,40,40);
//used to create the barriers
  walls1 = createSprite(random(725, 1154), (height/1.5),50,500);
  walls1.shapeColor = color(0);
  walls2 = createSprite(random(685, 650), (height/3.1),50, 500);
  walls2.shapeColor = color(0);
  walls3 = createSprite(random(200, 500), (height/2.1),500, 50);
  walls3.shapeColor = color(0);
  walls4 = createSprite(random(300, 500), (height/1.5),200, 100);
  walls4.shapeColor = color(0);
  wallsb = createSprite(10,1000,50,2080);
  wallsb.shapeColor = color(0);
  wallsb1 = createSprite(10,20,2580,50);
  wallsb1.shapeColor = color(0);
  wallsb2 = createSprite(10,880,2580,50);
  wallsb2.shapeColor = color(0);
  wallsb3 = createSprite(1270,1000,50,2080);
  wallsb3.shapeColor = color(0);






//Adds a timer to list of variables
  var timer = select('#timer');
    timer.html('0');
//function for timer to count up
  function timeIt(){
      counter ++;
      timer.html(counter);
    }
    setInterval(timeIt, 1000);// 1000ms = 1s

}
