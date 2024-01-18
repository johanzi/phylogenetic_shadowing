phylogenetic_shadowing
===

Pipeline to perform phylogenetic shadowing based on VISTA tools.

![](images/image4.png)

Example of phylogenetic shadowing between 6 related species from the Brassicaceae.


## In VISTA

* Go to http://pipeline.lbl.gov/cgi-bin/gateway2
* Select the clade and species (e.g. Plant, Arabidopsis thaliana)
* Enter as position the locus of interest (e.g. for FT, chr1:24331428-24333934)
* Select VISTA-Point mode for visualization

![](images/image1.png)

* Add then the desired species with ‘add alignment’ button, click ‘Add’
 
![](images/image2.png)

* Open in a new tab the file MFA indicated in the ‘Tools’ window
 
![](images/image3.png)

* Copy-paste the content in a text file
* Do the same for the other alignment but omit the first sequence which is already present (e.g. Arabidopsis thaliana). See [BlockE_conserved.txt](example/BlockE_conserved.txt).
* Change the name of the sequence so that it contains no spaces (error in Clustal Omega alignment) nor dots (error in BoxShade). The title should contain maximum 16 characters to be displayed fully once processed in BoxShade (e.g. “>Drummond's rockcress v.1.0 Scaffold26959:3697497-3698805 (-)” becomes “>B_stricta”)
* Put the alignments in the order wanted (the reference sequence is put first)

**Note**: VISTA tool provides scientific and vernacular plant names, which is not the best practice. Drummond's rockcress is *Arabidopsis drumondii*, also called *Boechera stricta*. They also have Turnip mustard and Napa cabbage which are the same species *Brassica rapa* but different cultivars (*Brassica rapa* subsp. *oleifera* and *Brassica rapa* subsp. *pekinensis*, respectively).

## In Clustal Omega

* Go to https://www.ebi.ac.uk/jdispatcher/msa/clustalo
* Choose ‘DNA’
* Copy paste the content of the text file with all species from VISTA `Input_Clustal_BlockE.txt` 
* In Step 2, click ‘More options’ and choose ‘input’ in the option ‘ORDER’ so that the order of the user is respected in the final display
* Submit the job
* Click on ‘Download Alignment File’ and save as `Output_Clustal_BlockE.aln`

Alternatively, one can use clustalw in the command line:
`clustalw -infile=Input_Clustal_BlockE.txt -OUTORDER=input -OUTFILE=Output_Clustal_BlockE.aln` and use the output file `Output_Clustal_BlockE.aln` in the next step

## In BoxShade

The webtool used here is based on [pyBoxshade](https://github.com/mdbaron42/pyBoxshade) and can also be run in the command line.

* Go to [https://junli.netlify.app/apps/boxshade/](https://junli.netlify.app/apps/boxshade/)
* Click "Choose file" and add `Output_Clustal_BlockE.aln`
* Select "CLUSTAL file" as input sequence format
* Select "RTF" as output format 
* Click "Start shading"
* File is automatically saved as `output.rdf`

The output should look like:

![](images/image4.png)



# Author

* Johan Zicola
