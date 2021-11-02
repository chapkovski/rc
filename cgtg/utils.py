from shutil import copyfile

src = './MyPage.html'

page_sequence = [
    "Consent",
    "GeneralInstructions",
    "RegionalInfoChoose",
    "RegionalInfoFixed",
    "CGInstructions",
    "CGquiz",
    "CGdecision",
    "CGBeliefsInstructions",
    "CGBeliefsquiz",
    "CGBeliefDecision",
    "Part2Announcement",
    "TGInstructions",
    "TGQuiz",
    "TGRoleAnnouncement",
    "TGDecision",
]

for p in page_sequence:
    copyfile(src, f'./{p}.html')
