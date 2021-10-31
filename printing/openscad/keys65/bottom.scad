

module my_board() {
    translate([0, 250, 0])
    union() {
        difference() {
        union() { 
            difference() {
                union() {
                    translate([.4   n ,0,0])
                    import("../../base_boards/sick68/files/Lower_-_Left.stl", convexity=3);
                    translate([-.3,0,0])
                    import("../../base_boards/sick68/files/Lower_-_Right.stl", convexity=3);
                }

                translate([-175, 20.28, 0])
                cube([350, 50, 25]);
            }
        }
        }
    }
}
my_board();
