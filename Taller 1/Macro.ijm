
run("8-bit");
setAutoThreshold("Default");
//run("Threshold...");
//setThreshold(0, 45);
setOption("BlackBackground", false);
run("Convert to Mask");
run("Close");
run("Find Edges");
run("Analyze Particles...", "  circularity=0.00-1.00 clear summarize in_situ");
