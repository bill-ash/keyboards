
module my_text() {
    union() {
        difference(){
                union() {
                    translate([.3,0,0])
                    import("../../base_boards/sick68/files/Upper_-_Left.stl", convexity=3);
                    translate([-.3,0,0])
                    import("../../base_boards/sick68/files/Upper_-_Right.stl", convexity=3);
                }
                    translate([-175, -87.32, 0])
                    cube([350, 120, 25]);
        }
    }
}

module my_board() {
    union() {
        difference() {
        union() { 
            difference() {
                union() {
                    translate([.3,0,0])
                    import("../../base_boards/sick68/files/Upper_-_Left.stl", convexity=3);
                    translate([-.3,0,0])
                    import("../../base_boards/sick68/files/Upper_-_Right.stl", convexity=3);
                }

                translate([-175, 20.28, 0])
                cube([350, 50, 25]);
            }

            translate([0, 19.01, 0])
            difference(){
                union() {
                    translate([.3,0,0])
                    import("../../base_boards/sick68/files/Upper_-_Left.stl", convexity=3);
                    translate([-.3,0,0])
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
        translate([97, 22, 10])
        cube([34, 25, 4.04]);

        // left block 
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
    }
}

// Full Board 
translate([0,200,0])
union() {
    difference() {
        // color([1,0,0])
        my_board();
            union() {
                // Cut left end 
                translate([-163.4, -90, 0])
                cube([7, 150, 30]);
                //  cut right end 
                mirror([1,0,0])
                translate([-156.59, -90, 0])
                cube([7, 150, 30]);

                // corner cutouts 
                union() {
                    
                    // bottom left 
                    translate([-159, -81, 0])
                    cube([7, 6, 30]);
                
                    // top left 
                    translate([-160, 44.5, 0])
                    cube([7, 9, 30]);

                
                // top right
                translate([142, 44, 0])
                cube([10, 10, 30]);

                // bottom right 
                translate([143, -81, 0])
                cube([7, 6, 30]);
                }
            }
    }
        // Fill corner gaps 
        // top right
        color([1,0,0])
        translate([142, 44, 10])
        cube([6, 5, 10]);
        
        // Bottom right
        color([1,0,0])
        color([1,0,0])
        translate([139.4, -76, 10])
        cube([10, 1.9, 10]);
        
        
        // top left
        mirror([1,0,0])
        color([1,0,0])
        translate([149, 44, 10])
        cube([6, 5, 10]);
        
        // Bottom Left 
        mirror([1,0,0])
        color([1,0,0])
        translate([146.2, -76, 10])
        cube([10, 1.9, 10]);
                

    translate([5, 0, 0])
    difference() {
        my_board();
        translate([-161.2, -76, 0])
        cube([320, 120, 30]);
        
        translate([-120, -90, 0])
        cube([320, 150, 30]);
    }

    mirror([1,0,0])
    translate([11.8, 0, 0])
    difference() {
        my_board();
        translate([-161.2, -76, 0])
        cube([320, 120, 30]);
        
        translate([-120, -90, 0])
        cube([320, 150, 30]);
    }



}