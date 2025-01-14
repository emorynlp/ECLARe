# -*- coding:utf-8 -*-
# Author: hankcs
# Date: 2021-05-27 20:14
import json

import elit
import eclare

classifier = elit.load(eclare.BINARY_BASELINE)
rchili_sample = {
    "ResumeFileName": "40431.docx",
    "Qualification": "Several years' experience in chart review and data collection \r Solid Infectious Disease and Oncology background in research studies and clinical trials \r Several years' experience in the clinical research industry \r Strong skills in ICD-CM coding \r Several years' experience working in Revenue Cycle Management \r Certified Risk Adjustment Coder \r Sound knowledge of Medicare Risk Adjustment / HCC coding compliance\r\r\rKeller Graduate School of Management, Chicago, Illinois \r Masters' of Business Administration - Health Services Management \r DeVry University, Atlanta, GA \r Bachelors of Science in Technical Management \r Wayne Community College, Goldsboro, NC \r Associates of Science in Human Services Technology",
    "SegregatedQualification": [
        {
            "Institution": {
                "Name": "DeVry University",
                "Type": "University",
                "ConfidenceScore": 7,
                "Location": {
                    "City": "Atlanta",
                    "State": "GA",
                    "StateIsoCode": "US-GA",
                    "Country": "USA",
                    "CountryCode": {
                        "IsoAlpha2": "US",
                        "IsoAlpha3": "USA",
                        "UNCode": "840"
                    }
                }
            },
            "SubInstitution": {
                "Name": "Keller Graduate School of Management",
                "ConfidenceScore": 8,
                "Type": "School",
                "Location": {
                    "City": "Chicago",
                    "State": "Illinois",
                    "StateIsoCode": "US-IL",
                    "Country": "USA",
                    "CountryCode": {
                        "IsoAlpha2": "US",
                        "IsoAlpha3": "USA",
                        "UNCode": "840"
                    }
                }
            },
            "Degree": {
                "DegreeName": "Masters' of Business Administration-Health Services Management",
                "NormalizeDegree": "Master of Business Administration",
                "Specialization": [
                    "Health Services Management"
                ],
                "ConfidenceScore": 8
            },
            "FormattedDegreePeriod": "",
            "StartDate": "",
            "EndDate": "",
            "Aggregate": {
                "Value": "",
                "MeasureType": ""
            }
        },
    ],
    "Certification": "\r\rCertified Risk Adjustment Coder (CRC) Year 2016 \r Certified Revenue Integrity Professional (CRIP) to Obtain 7/2018\r",
    "Experience": "EMORY HEALTHCARE, INC, ATLANTA, GA \r Clinical Trials Compliance / Billing Specialist (2013-Present) \r Conducts chart reviews on patient records enrolled on clinical trials to verify accuracy of diagnosis coding. \r Research documentation, coding and billing needs - including but not limited to daily charge-capture, audit inquires, and billing enhancement opportunities. \r Responds to compliance issues with details, analysis, and recommendations related to documentation, coding and process changes. \r Participates in the planning and development of tools used throughout the department to reconcile, audit, analyze, and report revenue cycle data. \r EMORY UNIVERSITY WINSHIP CANCER INSTITUTE, ATLANTA, GA \r Clinical Research Coordinator II - III (2007-2013) \r Provided overall coordination of clinical trials activities within the disease site team. \r Monitored and documented ongoing GCP and training by staff and reported progress to the designated supervisor on a regular basis. \r Conducted random audits of data completion of team at least weekly. \r Reconcile audit findings by external audit reports during external monitoring visits and report compliance issues to principal investigator. \r Coordinated and conducted patient care visits and assured all procedures were conducted within guidelines of the clinical research protocol \r Responsible for completion of study documentation forms, including case report forms and other study specific documents. \r Managed multiple global and regional clinical trials. \r Interacted with principal investigator as needed to assure patients received appropriate medical evaluation when needed and alerted principal investigator of serious adverse events. \r AIDS RESEARCH CONSORTIUM OF ATLANTA, ATLANTA, GA \r Research Associate (1998-2007) \r Responded to Quality Assurance audits to address necessary issues and ensure compliance. \r Prepared documents for submission to regulatory authorities and approval processes. \r Maintained records and reports for program evaluation activities. \r Trained data abstractors and ensured quality and integrity of study data was collected per guidelines and procedures of study protocol. \r Abstracted data from medical records following established procedures per research studies. \r  \r EMORY UNIVERSITY SCHOOL PUBLIC HEALTH, ATLANTA, GA \r Oncology Data Specialist / Abstractor (1987-1998) \r Identified reportable cancer cases per standard and criteria. \r Abstracted medical records on patients diagnosed with cancer. \r Search records of private laboratories, radiotherapy units, nursing homes, and other health services to ensure complete ascertainment of data. \r Maintained a data collection system organized to provide life time follow up of patients diagnosed with cancer.",
    "SegregatedExperience": [
        {
            "Employer": {
                "EmployerName": "EMORY HEALTHCARE, INC",
                "FormattedName": "",
                "ConfidenceScore": 10
            },
            "JobProfile": {
                "Title": "Clinical Trials Compliance/Billing Specialist",
                "FormattedName": "Billing specialist",
                "Alias": "billing specialist i, billing specialist ii, billing tech ii, Specialist Billing",
                "RelatedSkills": [
                    {
                        "Skill": "BillingTracker Pro",
                        "ProficiencyLevel": "Proficient"
                    },
                    {
                        "Skill": "PaySimple",
                        "ProficiencyLevel": "Moderate"
                    },
                    {
                        "Skill": "Expenses Management Software",
                        "ProficiencyLevel": "Moderate"
                    },
                    {
                        "Skill": "TEMNet Software",
                        "ProficiencyLevel": "Moderate"
                    },
                    {
                        "Skill": "Bill of Material",
                        "ProficiencyLevel": "Moderate"
                    },
                    {
                        "Skill": "Payment Analytics",
                        "ProficiencyLevel": "Moderate"
                    },
                    {
                        "Skill": "Recurring Billing",
                        "ProficiencyLevel": "Moderate"
                    },
                    {
                        "Skill": "Billing Software",
                        "ProficiencyLevel": "Proficient"
                    },
                    {
                        "Skill": "Cash Handling",
                        "ProficiencyLevel": "Proficient"
                    }
                ],
                "ConfidenceScore": 10
            },
            "Location": {
                "City": "ATLANTA",
                "State": "GA",
                "StateIsoCode": "US-GA",
                "Country": "USA",
                "CountryCode": {
                    "IsoAlpha2": "US",
                    "IsoAlpha3": "USA",
                    "UNCode": "840"
                }
            },
            "JobPeriod": "2013 - till",
            "FormattedJobPeriod": "2013 to till",
            "StartDate": "01/01/2013",
            "EndDate": "05/02/2021",
            "IsCurrentEmployer": "true",
            "JobDescription": "Conducts chart reviews on patient records enrolled on clinical trials to verify accuracy of diagnosis coding. \n Research documentation, coding and billing needs - including but not limited to daily charge-capture, audit inquires, and billing enhancement opportunities. \n Responds to compliance issues with details, analysis, and recommendations related to documentation, coding and process changes. \n Participates in the planning and development of tools used throughout the department to reconcile, audit, analyze, and report revenue cycle data.",
            "Projects": [
                {
                    "UsedSkills": "",
                    "ProjectName": "",
                    "TeamSize": ""
                }
            ]
        },
    ],
    "CurrentEmployer": "EMORY HEALTHCARE, INC",
    "JobProfile": "Clinical Trials Compliance/Billing Specialist",
    "WorkedPeriod": {
        "TotalExperienceInMonths": "446",
        "TotalExperienceInYear": "37.2",
        "TotalExperienceRange": "GREATER THAN 10 YEAR"
    },
}

rchili_sample.update({
    "applied_job_title": "CRCI",
    "applied_job_description": "Handles or assists with administrative activities generally associated with the conduct of clinical trials. Maintains data pertaining to research projects, completes source documents/case report forms, and performs data entry. Assists with patient recruitment. Attends study meetings. Orders and maintains equipment and supplies. Reviews medical records and/or conducts screenings for recruitment of study participants, performs interviews and QOL questionnaires. Collects study specimen according to protocol which may include phlebotomy, processing, and preparation for shipping. Coordinates services, schedules procedures, creates and maintains case packages, and monitors charges. Assists with quality assurance and tracks regulatory submissions. Performs related approved responsibilities as required.   MINIMUM QUALIFICATIONS: (1.) High School Diploma or GED and three years of administrative support experience OR (2.) Two years of college in a scientific, health related, or business administration program and one year of admin support or customer service experience OR (3.) Licensed as a practical nurse (LPN) and one year admin support or one year of licensed practical nursing experience OR (4.) Bachelor's degree, Master's degree, MD or PhD in a scientific, health related or business administration program.   This position is intended to support clinical research and all clinical training requirements must be tracked and monitored through Emory Healthcare under the credentialing category of CLINICAL RESEARCHER.",
})
accept = classifier([rchili_sample])
print(json.dumps(accept, indent=2))
