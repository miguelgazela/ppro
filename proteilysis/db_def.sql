#--------------------------------------------------------
#                 PROTEINS AND COMPONENTS 
#--------------------------------------------------------

drop table if exists Protein;
drop table if exists Helix;
drop table if exists Sheet;
drop table if exists Sequence;

create table Protein (
    id          SERIAL,
    PRIMARY KEY(id)
);

create table Helix (
    id          SERIAL,
    proteinID   BIGINT UNSIGNED NOT NULL,
    comment     VARCHAR(255),
    helixClass  INT UNSIGNED NOT NULL,
    endICode    CHAR(1) NOT NULL,
    helixID     VARCHAR(3) NOT NULL,
    endSeqNum   INT UNSIGNED NOT NULL,
    initSeqNum  INT UNSIGNED NOT NULL,
    initResName VARCHAR(3) NOT NULL,
    serNum      INT UNSIGNED NOT NULL,
    initChainID CHAR(1) NOT NULL,
    initICode   CHAR(1) NOT NULL,
    lenght      INT UNSIGNED NOT NULL,
    endChainID  CHAR(1) NOT NULL,
    endResName  VARCHAR(3) NOT NULL,
    type        enum('Right-handed alpha (default)', 'Right-handed omega', 'Right-handed pi', 'Right-handed gamma', 'Right-handed 3 - 10', 'Left-handed alpha', 'Left-handed omega', 'Left-handed gamma', '2 - 7 ribbon/helix', 'Polyproline') NOT NULL,
    PRIMARY KEY(id)
);

create table Sheet (
    id          SERIAL,
    proteinID   BIGINT UNSIGNED NOT NULL,
    strand      INT UNSIGNED NOT NULL,
    sheetID     VARCHAR(3) NOT NULL,
    numStrands  INT UNSIGNED NOT NULL,
    initResName VARCHAR(3) NOT NULL,
    initChainID CHAR(1) NOT NULL,
    initSeqNum  INT UNSIGNED NOT NULL,
    initICode   CHAR(1) NOT NULL,
    endResName  VARCHAR(3) NOT NULL,
    endChainID  CHAR(1) NOT NULL,
    endSeqNUm   INT UNSIGNED NOT NULL,
    endICode    CHAR(1) NOT NULL,
    sense       INT UNSIGNED NOT NULL,
    curAtom     VARCHAR(3),
    curResName  VARCHAR(3),
    curChainID  CHAR(1),
    curResSeq   INT UNSIGNED,
    curICode    CHAR(1),
    prevAtom    VARCHAR(3),
    prevResName VARCHAR(3),
    prevChainID CHAR(1),
    prevResSeq  INT UNSIGNED,
    prevICode   CHAR(1),
    PRIMARY KEY(id)
);

create table Sequence (
    id          SERIAL,
    proteinID   BIGINT UNSIGNED NOT NULL,
    serNum      INT UNSIGNED NOT NULL,
    chainID     CHAR(1) NOT NULL,
    numRes      INT UNSIGNED NOT NULL,
    Residues    VARCHAR(51) NOT NULL,
    PRIMARY KEY(id)
);