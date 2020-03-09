r=60;
a=5;
alpha=15;
alpha2=145;
g=1;//gradient
//
r1=20; //bottom radius
l = r1*sqrt(3);
p1 = [-l/2,-l/sqrt(3)/2];
p2 = [l/2, -l/sqrt(3)/2];
p3 = [0, l/sqrt(3)];
times=3;
module sphe(al_x,al_z,r){
    rotate([al_x,0,al_z])
    translate([0,0,-r])
    sphere(r=1.5);
}

module lattice(r){
    module rot(alpha){
        hull(){
            sphe(alpha,alpha/g,r);
            sphe(alpha+a,(alpha+a)/g,r);
        }
        hull(){
            sphe(-alpha,-alpha/g,r);
            sphe(-alpha-a,-(alpha+a)/g,r);
        }
        if(alpha<alpha2-a){
            rot(alpha+a);
        }
    }
    translate([0,0,r])
    for(i=[0:20:360]){
        rotate([0,0,i])
        rot(alpha);
    }
}

 module sierpinski(p1, p2, p3, times){
     function mid(ps, pe) = [(ps[0]+pe[0])/2, (ps[1]+pe[1])/2];
         
    linear_extrude(12,convexity=10)
    offset(delta=-0.1) 
    polygon([mid(p2,p3), mid(p1,p2), mid(p1,p3)]);
    if (times>0){
        sierpinski(p1, mid(p1,p2), mid(p1,p3), times-1);
        sierpinski(mid(p2,p1), p2, mid(p2,p3), times-1);
        sierpinski(mid(p3,p1), mid(p3,p2), p3, times-1);
    }  
}
module bottom(){
    union(){
    difference(){
        translate([0,0,0])
        cylinder(r=r1+5,h=30);
        translate([0,0,10])
        cylinder(r=r1,h=30);
    }
       translate([0,0,0])
       sierpinski(p1,p2,p3,3); 
        
   } 
}

module topsur(r){
    translate([0,0,r])
    difference(){
        sphere(r+1.5, $fn=60);
        sphere(r-1.5, $fn=60);
        cylinder(2*r,r/2,r/2, center=false,$fn=60);
        rotate(180,v=[0,1,0])
        translate([0,0,-r/2*sqrt(3)+5])
        cylinder(2*r,2*r,2*r, center=false);
    } 
}

module patt(){
    module quad(){
        //translate([r,0,0])
        linear_extrude(r+20,convexity=10)
        translate([1.5,0,0])
    
            scale([2,1])
            circle(1,$fn=4);           
    }
    translate([0,0,0])
    rotate([0,-90,0])
    for(ii=[0:2]){
        rotate(ii*120,v=[0,0,1])
        quad();  
    }
}

module top1(){
     for(kk=[0:30:360]){
         translate([0,0,r/2*sqrt(3)-3])
        rotate([0,0,kk])
        rotate([0,60,0])
        patt();   
    }
}

module top(){
    difference(){
        topsur(r);
        top1();
    } 
}

module final(){
    top();
    lattice(r);
    rotate([0,0,15])
    lattice(r);
    bottom();  
}
final();
