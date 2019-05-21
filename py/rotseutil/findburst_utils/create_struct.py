'''
Created on Jul 18, 2017

@author: Daniel Sela, Arnon Sela
'''


def create_struct(strname, tagnames, tag_descript, dimen=1, chatter=0, nodelete=None):
    '''
    ;+
    ; NAME:
    ;       CREATE_STRUCT
    ; PURPOSE:
    ;       Create an IDL structure from a list of tag names and dimensions
    ; EXPLANATION:
    ;       Dynamically create an IDL structure variable from list of tag names
    ;       and data types of arbitrary dimensions.   Useful when the type of
    ;       structure needed is not known until run time.
    ;
    ;       Unlike the intrinsic function CREATE_STRUCT(), this procedure does not
    ;       require the user to know the number of tags before run time.   (Note
    ;       there is no name conflict since the intrinsic CREATE_STRUCT is a
    ;       function, and this file contains a procedure.)
    ; CALLING SEQUENCE:
    ;       CREATE_STRUCT, STRUCT, strname, tagnames, tag_descript,
    ;                             [ DIMEN = , /CHATTER, /NODELETE ]
    ;
    ; INPUTS:
    ;       STRNAME -   name to be associated with structure (string)
    ;               Must be unique for each structure created.   Set
    ;               STRNAME = '' to create an anonymous structure
    ;
    ;       TAGNAMES -  tag names for structure elements
    ;               (string or string array)
    ;
    ;       TAG_DESCRIPT -  String descriptor for the structure, containing the
    ;               tag type and dimensions.  For example, 'A(2),F(3),I', would
    ;               be the descriptor for a structure with 3 tags, strarr(2),
    ;               fltarr(3) and Integer scalar, respectively.
    ;               Allowed types are 'A' for strings, 'B' or 'L' for unsigned byte
    ;               integers, 'I' for integers, 'J' for longword integers,
    ;               'F' or 'E' for floating point, 'D' for double precision
    ;               'C' for complex, and 'M' for double complex
    ;               Uninterpretable characters in a format field are ignored.
    ;
    ;               For vectors, the tag description can also be specified by
    ;               a repeat count.  For example, '16E,2J' would specify a
    ;               structure with two tags, fltarr(16), and lonarr(2)
    ;
    ; OPTIONAL KEYWORD INPUTS:
    ;       DIMEN -    number of dimensions of structure array (default is 1)
    ;
    ;       CHATTER -  If /CHATTER is set, then CREATE_STRUCT will display
    ;                  the dimensions of the structure to be created, and prompt
    ;                  the user whether to continue.  Default is no prompt.
    ;
    ;       NODELETE - If /NODELETE is set, then the temporary file created
    ;                  CREATE_STRUCT will not be deleted upon exiting.   See below
    ;
    ; OUTPUTS:
    ;       STRUCT -   IDL structure, created according to specifications
    ;
    ; EXAMPLES:
    ;
    ;       IDL> create_struct, new, 'name',['tag1','tag2','tag3'], 'D(2),F,A(1)'
    ;
    ;       will create a structure variable new, with structure name NAME
    ;
    ;       To see the structure of new:
    ;
    ;       IDL> help,new,/struc
    ;       ** Structure NAME, 3 tags, 20 length:
    ;          TAG1            DOUBLE         Array(2)
    ;          TAG2            FLOAT          0.0
    ;          TAG3            STRING         Array(1)
    ;
    ; PROCEDURE:
    ;       Generates a temporary procedure file using input information with
    ;       the desired structure data types and dimensions hard-coded.
    ;       This file is then executed with CALL_PROCEDURE.
    ;
    ; NOTES:
    ;       If CREATE_STRUCT cannot write a temporary .pro file in the current
    ;       directory, then it will write the temporary file in the getenv('HOME')
    ;       directory.
    ;
    ;       At present, can fail if a tag_name cannot be used as a proper
    ;       structure component definition, e.g., '0.10' will not
    ;       work, but a typical string like 'RA' or 'DEC' will.
    ;       A partial workaround checks for characters '\' and '/'
    ;       and '.' and converts them to '_'. in a tag_name.
    ;
    ;       Note that 'L' now specifies a LOGICAL (byte) data type and not a
    ;       a LONG data type for consistency with FITS binary tables
    ;
    ; RESTRICTIONS:
    ;       The name of the structure must be unique, for each structure created.
    ;       Otherwise, the new variable will have the same structure as the
    ;       previous definition (because the temporary procedure will not be
    ;       recompiled).  ** No error message will be generated  ***
    ;
    ; SUBROUTINES CALLED:
    ;       FDECOMP, REPCHR()
    ;
    ; MODIFICATION HISTORY:
    ;       Version 1.0 RAS January 1992
    ;       Modified 26 Feb 1992 for Rosat IDL Library (GAR)
    ;       Modified Jun 1992 to accept arrays for tag elements -- KLV, Hughes STX
    ;       Accept anonymous structures W. Landsman  HSTX    Sep. 92
    ;       Accept 'E' and 'J' format specifications   W. Landsman Jan 93
    ;       'L' format now stands for logical and not long array
    ;       Accept repeat format for vectors        W. Landsman Feb 93
    ;       Accept complex and double complex (for V4.0)   W. Landsman Jul 95
    ;       Work for long structure definitions  W. Landsman Aug 97
    ;       Converted to IDL V5.0   W. Landsman   September 1997
    ;       Write temporary file in HOME directory if necessary  W. Landsman Jul 98
    ;       Use OPENR,/DELETE for OS-independent file removal W. Landsman Jan 99
    ;       Use STRSPLIT() instead of GETTOK() W. Landsman  July 2002
    ;-
    ;-------------------------------------------------------------------------------
    '''
