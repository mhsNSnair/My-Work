//sets counter to 0
let counter = 0;

function setup() {
//Canvas size 1280 by 899
  createCanvas(1280,899);
  //used to create the objective
  boxes = createSprite(random(90, 100), random(600, 700),25, 25);
  boxes.shapeColor = color(255, 0, 0);
  //used to create the player
  player = createSprite(100, 700, 40, 40);
  player.shapeColor = color(255);
//used to create the end
  win = createSprite(random(600,610), random(350,370),25, 25);
  win.shapeColor = color(0,255,0);
  //used to create the barriers
  walls1 = createSprite(random(600, 700), (270),1000,50);
  walls1.shapeColor = color(0);
  walls2 = createSprite(random(645, 650), (400),50, 600);
  walls2.shapeColor = color(0);
  walls3 = createSprite(random(300, 360), (height/2.1),600, 50);
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
