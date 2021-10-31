
module my_text() {
    union() {
        difference(){
                union() {
                    import("../../base_boards/sick68/files/Upper_-_Left.stl", convexity=3);
                    import("../../base_boards/sick68/files/Upper_-_Right.stl", convexity=3);
                }
                    translate([-175, -87.32, 0])
                    cube([350, 120, 25]);
        }
    }
}



union() {
    difference() {
    union(){
        difference() {
            union() {
                import("../../base_boards/sick68/files/Upper_-_Left.stl", convexity=3);
                import("../../base_boards/sick68/files/Upper_-_Right.stl", convexity=3);
            }

            translate([-175, 20.28, 0])
            cube([350, 50, 25]);
        }

        translate([0, 19.01, 0])
        difference(){
            union() {
                import("../../base_boards/sick68/files/Upper_-_Left.stl", convexity=3);
                import("../../base_boards/sick68/files/Upper_-_Right.stl", convexity=3);
            }

                translate([-175, -80, 0])
                color([1, 0, 0])
                cube([350, 81.14, 25]);

        }
    }

        color([0,1,1])
        translate([-135,22,9])
        cube([265, 19, 10]);
        
        translate([-160, 45, 19.99])
        cube([70, 10, 10]);

        translate([-170, 47, 0])
        cube([100,20,22]);
    }

    // right block
    // color([0,1,0])
    translate([97, 22, 10])
    cube([34, 25, 4.04]);

    // left block 
    // color([0,1,0])
    translate([-136, 22, 10])
    cube([7, 25, 4.04]);

    translate([25, 19.01, 0])
    union() {
        // Function keys
        difference(){
                union() {
                    import("../../base_boards/sick68/files/Upper_-_Left.stl", convexity=3);
                    import("../../base_boards/sick68/files/Upper_-_Right.stl", convexity=3);
                }

                    translate([-175, -80, 0])
                    cube([350, 81.14, 25]);

            union() {

                translate([-170, 23.5, 0])
                cube([330, 25, 25]);

                translate([-175, 0, 0])
                cube([20, 25, 25]);

                
            }   
            translate([75, 0, 0])
            cube([90, 25, 25]);
        }
    }
}


translate([120,18.,0])
union() {
    difference() {
        union() {
            my_text();
            translate([-260, 0, 0])
            mirror([1,0,0])
            my_text();

        }
        translate([-180, 20, 20.001])
        cube([100, 20, 10]);
    }
}



translate([-0, 10, 0])
difference() {
    my_text();
    translate([-180, 30, 10])
    cube([100,6.5,20]);

}
translate([30, 10, 0])
difference() {
    my_text();
    translate([-180, 30, 10])
    cube([100,6.5,20]);

}
translate([-39, 47, 18])
linear_extrude(4)
text("BillBikes", font = "Liberation Sans:style=Bold Italic");