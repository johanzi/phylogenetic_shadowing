# phylogenetic_shadowing



Pipeline to perform phylogenetic shadowing based on VISTA tools.


## In VISTA

* Go to http://pipeline.lbl.gov/cgi-bin/gateway2
* Select the clade and species (e.g. Plant, Arabidopsis thaliana)
* Enter as position the locus of interest (e.g. for FT, chr1:24331428-24333934)
* Select VISTA-Point mode for visualization

* Add then the desired species with ‘add alignment’ button, click ‘Add’
 
* Open in a new tab the file MFA indicated in the ‘Tools’ window
 
* Copy-paste the content in a notepad file
* Do the same for the other alignment but omit the first sequence which is already present (e.g. Arabidopsis thaliana)
* Change the name of the sequence so that no dots or spaces are present (e.g. “>Drummond's rockcress v.1.0 Scaffold26959:3697497-3698805 (-)” becomes “>B_stricta”) and that the title contains maximum 16 characters (to be fully displayed once processed in BoxShade)
* Put the alignments in the order wanted (the reference sequence is put first)

## In Clustal Omega

* Go to http://www.ebi.ac.uk/Tools/msa/clustalo/
* Choose ‘DNA’
* Copy paste the content of the text file with all species from VISTA
* In Step 2, click ‘More options’ and choose ‘input’ in the option ‘ORDER’ so that the order of the user is respected in the final display
* Submit the job
* Click on ‘Download Alignment File’
* To be processed in BoxShad, the file needs to be modified. For this, the script clustalOmega2BoxShade.py (see below) can be used on a Linux/Unix system with Python 2.7 installed. The script converts the Clustal output into a FASTA format 
* Enter in command line: `python clustalOmega2BoxShade.py <input.file> > <output.file>`
* The content of the output file can be used in BoxShade webtool

## In BoxShade

* Go to http://www.ch.embnet.org/software/BOX_form.html
* Select ‘RTF_new’ as output format 
* Select as ‘ALN’ as input sequence format
* Copy and paste the content of the output.file in the input box
* Download the output RTF file (can be opened in Word and exported as pdf)






