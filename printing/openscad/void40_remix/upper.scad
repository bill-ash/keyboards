// Refactor upper for itsy-bitsy

difference() {
    import("../../base_boards/void40/files/VOID40OP_-_Top_GRID.stl", convexity=3);
    union() {
        translate([-10, -23.9, 1.55])
        cube([250, 130, 10]);
    }
    }
    