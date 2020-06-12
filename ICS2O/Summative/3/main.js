//sets counter to 0
let counter = 0;

function setup() {
//Canvas size 1280 by 899
  createCanvas(1280,899);

//used to create the objective
  boxes = createSprite(random(200, 280), random(600,639),25, 25);
  boxes.shapeColor = color(255, 0, 0);
  //used to create the player
  player = createSprite(random(200, 280), random(800,839), 40, 40);
  player.shapeColor = color(255);
  //used to create the end
  win = createSprite(random(200, 280), random(800,839),25, 25);
  win.shapeColor = color(0,255,0);
  //used to create the barriers
  walls1 = createSprite(random(490, 500), (450,464),50,600);
  walls1.shapeColor = color(0);
  walls2 = createSprite(random(772, 773), (130,150),600, 50);
  walls2.shapeColor = color(0);
  walls3 = createSprite(random(200, 300), (700,739),500, 50);
  walls3.shapeColor = color(0);
  walls4 = createSprite(random(870, 900), (450),random(0,680),random(0,445));
  walls4.shapeColor = color(0);
  walls5 = createSprite(random(760, 870), (550,600),550, 50);
  walls5.shapeColor = color(0);
  walls6 = createSprite(random(925, 975), (735,740),620, 50);
  walls6.shapeColor = color(0);
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
