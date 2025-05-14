# decision_tree.py

symptom_tree = {
    "Anxiety": {
        "Social Anxiety": {
            "In Public Places": {
                "Crowded Streets": {
                    "Feeling Watched": {
                        "diagnosis": (
                            "You may be experiencing symptoms of social anxiety, especially hypervigilance in crowded environments. "
                            "This can manifest as a constant feeling of being observed or judged, even without clear cause. "
                            "Techniques such as grounding (e.g., naming 5 things you see, 4 you can touch, etc.) and cognitive restructuring "
                            "can be helpful in reducing this perception over time."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/social-anxiety-disorder/symptoms-causes/syc-20353561"
                    },
                    "Avoiding Eye Contact": {
                        "diagnosis": (
                            "Avoiding eye contact in public spaces is a common behavioral symptom of social anxiety. "
                            "It typically arises from fear of confrontation, embarrassment, or perceived judgment. "
                            "Gradual exposure therapy and confidence-building exercises can help increase comfort with eye contact over time."
                        ),
                        "link": "https://www.nimh.nih.gov/health/publications/social-anxiety-disorder-more-than-just-shyness"
                    }
                },
                "Shopping Malls": {
                    "Fear of Bumping into People": {
                        "diagnosis": (
                            "This fear reflects an anxious response to unpredictability in crowded areas. "
                            "Individuals may feel overwhelmed by the lack of personal space or fear causing a scene. "
                            "Therapies focusing on desensitization and space awareness, paired with off-peak exposure, are often beneficial."
                        ),
                        "link": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5573566/"
                    },
                    "Panic in Long Queues": {
                        "diagnosis": (
                            "Waiting in line can trigger feelings of helplessness or entrapment in people with anxiety. "
                            "This can escalate to panic symptoms such as chest tightness or dizziness. "
                            "Relaxation techniques, breathing exercises, or having a distraction (like music) can help manage the stress."
                        ),
                        "link": "https://www.anxiety.org/panic-disorder"
                    }
                }
            },
            "Speaking in Groups": {
                "Presentations at Work": {
                    "Sweaty Palms": {
                        "diagnosis": (
                            "Sweaty palms during public speaking are a classic physical symptom of performance anxiety. "
                            "It’s caused by the body’s fight-or-flight response. "
                            "Deep breathing, preparation, and practicing with a trusted group can reduce physiological arousal."
                        ),
                        "link": "https://www.apa.org/topics/anxiety"
                    },
                    "Forgetting Words": {
                        "diagnosis": (
                            "Memory lapses during presentations often stem from heightened self-awareness and fear of evaluation. "
                            "Anxiety can interrupt working memory, making it harder to retrieve words under pressure. "
                            "Rehearsing in front of others or using memory cues can help restore flow."
                        ),
                        "link": "https://adaa.org/understanding-anxiety/social-anxiety-disorder"
                    }
                },
                "Group Discussions": {
                    "Fear of Judgment": {
                        "diagnosis": (
                            "Fear of judgment in social settings is a hallmark of social anxiety. "
                            "It involves overestimating negative evaluation from others, leading to avoidance or hesitancy. "
                            "Cognitive behavioral therapy (CBT) can help reframe these thought patterns and build assertiveness."
                        ),
                        "link": "https://www.nhs.uk/mental-health/conditions/social-anxiety/"
                    },
                    "Self-Doubt": {
                        "diagnosis": (
                            "Persistent self-doubt in group conversations can stem from low self-esteem or previous negative experiences. "
                            "It often leads to overthinking or withdrawal. Techniques like positive self-talk and guided role-play may improve confidence."
                        ),
                        "link": "https://psychcentral.com/anxiety/social-anxiety-and-self-doubt"
                    }
                }
            }
        },
        "Generalized Anxiety": {
            "Work Stress": {
                "Deadlines": {
                    "Insomnia": {
                        "diagnosis": (
                            "Trouble sleeping before deadlines may indicate performance-related anxiety. "
                            "Racing thoughts, physical restlessness, and difficulty relaxing are common. "
                            "Using structured planning during the day and calming bedtime routines can help."
                        ),
                        "link": "https://www.sleepfoundation.org/anxiety-and-sleep"
                    },
                    "Overthinking": {
                        "diagnosis": (
                            "Overthinking is a common cognitive symptom of anxiety, especially in high-pressure work environments. "
                            "It may involve replaying conversations or anticipating worst-case scenarios. "
                            "Mindfulness meditation and journaling are useful tools to quiet mental noise."
                        ),
                        "link": "https://psychcentral.com/anxiety/what-is-overthinking"
                    }
                },
                "Meetings": {
                    "Performance Fear": {
                        "diagnosis": (
                            "Fear of underperforming in meetings can cause anticipatory anxiety and physical symptoms. "
                            "It stems from internalized pressure to appear competent. "
                            "Preparation, supportive feedback, and exposure to low-stakes meetings can help."
                        ),
                        "link": "https://www.anxietycanada.com/articles/how-to-handle-performance-anxiety/"
                    },
                    "Avoidance": {
                        "diagnosis": (
                            "Avoiding meetings may be a coping mechanism to escape feelings of scrutiny or inadequacy. "
                            "While it provides temporary relief, it reinforces fear long-term. Gradual participation and goal-setting can reduce avoidance behaviors."
                        ),
                        "link": "https://adaa.org/understanding-anxiety/social-anxiety-disorder"
                    }
                }
            },
            "Family Issues": {
                "Financial Worries": {
                    "Restlessness": {
                        "diagnosis": (
                            "Financial stress often triggers chronic restlessness — pacing, fidgeting, or trouble focusing. "
                            "This is due to perceived threats to safety or stability. "
                            "Budgeting plans, financial counseling, and stress management techniques can reduce this response."
                        ),
                        "link": "https://www.apa.org/monitor/2019/02/money-stress"
                    },
                    "Irritability": {
                        "diagnosis": (
                            "Anxiety around finances may manifest as mood swings and irritability, especially during uncertainty. "
                            "Recognizing stress triggers and practicing self-regulation (breathing, exercise) are key strategies."
                        ),
                        "link": "https://www.healthline.com/health/anxiety/irritability"
                    }
                },
                "Conflict": {
                    "Mood Swings": {
                        "diagnosis": (
                            "Frequent emotional ups and downs in family settings can reflect underlying generalized anxiety. "
                            "Unpredictable conflict or tension heightens emotional reactivity. "
                            "Therapeutic communication and emotional labeling can help stabilize responses."
                        ),
                        "link": "https://www.mind.org.uk/information-support/types-of-mental-health-problems/anxiety-and-panic-attacks/"
                    },
                    "Withdrawal": {
                        "diagnosis": (
                            "Withdrawing from family interactions may be a defense against anxiety-related overwhelm. "
                            "Avoidance often leads to further emotional distance. Reconnecting through low-pressure activities may re-establish comfort."
                        ),
                        "link": "https://www.nimh.nih.gov/health/topics/anxiety-disorders"
                    }
                }
            }
        }
    },


    "Depression": {
        "Mild Depression": {
            "Occasional Sadness": {
                "Seasonal Triggers": {
                    "Less Daylight": {
                        "diagnosis": (
                            "You may be experiencing seasonal affective disorder (SAD), a form of depression that occurs during reduced daylight periods. "
                            "The lack of sunlight can affect circadian rhythms and serotonin levels, which contribute to mood regulation. "
                            "Light therapy and daily outdoor exposure in the morning are commonly recommended interventions."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/seasonal-affective-disorder/symptoms-causes/syc-20364651"
                    },
                    "Isolation": {
                        "diagnosis": (
                            "Feelings of sadness worsened by isolation are common in mild depression. "
                            "Humans are social beings, and lack of connection can contribute to low mood and decreased motivation. "
                            "Virtual check-ins, joining hobby groups, or scheduling brief interactions can help ease the sense of disconnection."
                        ),
                        "link": "https://www.nimh.nih.gov/health/topics/depression"
                    }
                },
                "Social Media Overuse": {
                    "Comparison Anxiety": {
                        "diagnosis": (
                            "Frequently comparing yourself to others on social media can trigger depressive thoughts and self-doubt. "
                            "This behavior reinforces unrealistic standards and undermines self-worth. "
                            "Reducing exposure and curating your feed to include uplifting or neutral content can support emotional balance."
                        ),
                        "link": "https://www.apa.org/news/press/releases/2022/10/social-media-mental-health"
                    },
                    "Fatigue": {
                        "diagnosis": (
                            "Constant scrolling can disrupt focus, reduce sleep quality, and lead to mental exhaustion — all contributing to low mood. "
                            "This type of fatigue often stems from overstimulation without emotional fulfillment. "
                            "Creating digital downtime and prioritizing offline relaxation can help restore energy."
                        ),
                        "link": "https://www.healthline.com/health/mental-health/social-media-and-depression"
                    }
                }
            },
            "Lack of Motivation": {
                "School/Work Tasks": {
                    "Delayed Assignments": {
                        "diagnosis": (
                            "Procrastination and missed deadlines may signal cognitive symptoms of depression such as low energy, indecisiveness, or lack of focus. "
                            "This often stems from overwhelm and internal criticism. "
                            "Breaking tasks into smaller goals and using tools like timers can improve follow-through."
                        ),
                        "link": "https://adaa.org/learn-from-us/from-the-experts/blog-posts/consumer/procrastination-and-anxiety"
                    },
                    "Missed Deadlines": {
                        "diagnosis": (
                            "When deadlines are consistently missed, it may reflect mental fatigue, executive dysfunction, or low self-efficacy. "
                            "This is common in people with mild depression. Supportive accountability and structured planning may improve task completion."
                        ),
                        "link": "https://www.verywellmind.com/executive-dysfunction-symptoms-causes-and-treatments-7117612"
                    }
                },
                "Hygiene Neglect": {
                    "Skipping Showers": {
                        "diagnosis": (
                            "Depression can impair daily functioning, including hygiene routines. "
                            "Low energy, reduced interest in self-care, and emotional numbness may lead to skipping showers. "
                            "Setting micro-goals (e.g., washing your face or brushing teeth) can be an effective first step."
                        ),
                        "link": "https://psychcentral.com/depression/depression-and-hygiene"
                    },
                    "Unchanged Clothes": {
                        "diagnosis": (
                            "Wearing the same clothes repeatedly may signal difficulty initiating basic self-care. "
                            "This behavior is common when motivation and interest drop significantly. "
                            "Laying out clean clothes the night before or asking for support from a friend may help create momentum."
                        ),
                        "link": "https://www.nimh.nih.gov/health/publications/depression"
                    }
                }
            }
        },

        "Major Depression": {
            "Persistent Low Mood": {
                "Every Day Sadness": {
                    "No Energy": {
                        "diagnosis": (
                            "A constant lack of energy, also called anergia, is a core symptom of major depressive disorder. "
                            "It's not just fatigue — it can feel like even basic actions require immense effort. "
                            "Gentle activities like stretching or walking can help gradually reintroduce movement and engagement."
                        ),
                        "link": "https://www.verywellmind.com/fatigue-and-depression-5181796"
                    },
                    "Hopelessness": {
                        "diagnosis": (
                            "Feelings of hopelessness — believing that nothing will improve — are a psychological hallmark of depression. "
                            "It is strongly correlated with suicidal ideation and emotional numbness. "
                            "Therapeutic intervention, especially cognitive-behavioral therapy, can help rebuild optimism and agency."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/depression/symptoms-causes/syc-20356007"
                    }
                },
                "Suicidal Thoughts": {
                    "Planning": {
                        "diagnosis": (
                            "If you're experiencing suicidal thoughts with a plan, this is a serious crisis requiring immediate attention. "
                            "These thoughts may feel isolating, but you are not alone. "
                            "Contact a crisis line, mental health professional, or trusted person as soon as possible. "
                            "Help is available and things can improve with support."
                        ),
                        "link": "https://988lifeline.org/"
                    },
                    "Withdrawing From Friends": {
                        "diagnosis": (
                            "Social withdrawal is a common behavioral symptom of depression, often tied to feelings of worthlessness or fatigue. "
                            "While being alone may seem easier, isolation can worsen mood. "
                            "Small acts like replying to one message or planning a short meetup can help rebuild connection."
                        ),
                        "link": "https://www.nimh.nih.gov/health/topics/depression"
                    }
                }
            },
            "Appetite Changes": {
                "Overeating": {
                    "Emotional Eating": {
                        "diagnosis": (
                            "Using food as a coping strategy for sadness, boredom, or emptiness is a common but maladaptive pattern. "
                            "This can lead to guilt and reinforce depressive cycles. "
                            "Mindful eating and emotional awareness tools can support healthier patterns."
                        ),
                        "link": "https://www.nationaleatingdisorders.org/learn/by-eating-disorder/other"
                    },
                    "Weight Gain": {
                        "diagnosis": (
                            "Significant weight gain during depressive episodes may reflect emotional eating or changes in metabolism due to inactivity. "
                            "This can affect self-image and worsen low mood. Balanced nutrition, gentle exercise, and emotional support are helpful."
                        ),
                        "link": "https://www.medicalnewstoday.com/articles/weight-gain-and-depression"
                    }
                },
                "Not Eating": {
                    "Nausea": {
                        "diagnosis": (
                            "Loss of appetite accompanied by nausea is common in major depression. "
                            "It may stem from hormonal disruption, stress, or lack of pleasure in eating. "
                            "Trying small, bland meals and eating on a schedule can help maintain basic nutrition."
                        ),
                        "link": "https://www.healthline.com/health/depression/appetite-loss"
                    },
                    "Weight Loss": {
                        "diagnosis": (
                            "Unintentional weight loss is a key diagnostic marker for major depressive disorder. "
                            "It often results from low appetite, digestive changes, or neglecting meals. "
                            "If weight loss is persistent, consult a healthcare provider to rule out other causes."
                        ),
                        "link": "https://www.ncbi.nlm.nih.gov/books/NBK546593/"
                    }
                }
            }
        }
    },


    "Stomach Pain": {
        "Upper Abdominal": {
            "Acid Reflux": {
                "Spicy Foods": {
                    "Burning Sensation": {
                        "diagnosis": (
                            "Spicy foods can irritate the esophagus and stomach lining, triggering acid reflux and a burning sensation in the chest or throat. "
                            "This discomfort typically occurs shortly after eating and may be worsened by lying down. "
                            "Avoiding spicy meals and eating smaller portions may reduce symptoms."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/acid-reflux/diagnosis-treatment/drc-20361960"
                    },
                    "Sour Taste": {
                        "diagnosis": (
                            "A sour or bitter taste in the mouth after eating spicy or acidic foods may result from stomach acid backing up into the esophagus (acid reflux). "
                            "This symptom is often accompanied by burping, bloating, or a sore throat. "
                            "Antacids and avoiding trigger foods can help manage it."
                        ),
                        "link": "https://www.clevelandclinic.org/health/diseases/17691-gerd"
                    }
                },
                "Lying Down Post-Eating": {
                    "Regurgitation": {
                        "diagnosis": (
                            "Lying flat after meals can cause stomach contents to move backward into the esophagus, leading to regurgitation or the sensation of food coming back up. "
                            "This is a common symptom of GERD. Waiting 2–3 hours after eating before lying down is advised."
                        ),
                        "link": "https://www.hopkinsmedicine.org/health/conditions-and-diseases/gastroesophageal-reflux-disease-gerd"
                    },
                    "Burping": {
                        "diagnosis": (
                            "Frequent burping after meals may indicate swallowed air or excess gas production related to reflux or indigestion. "
                            "It can be worsened by carbonated drinks, gum chewing, or eating too quickly. "
                            "Smaller, slower meals may help reduce burping."
                        ),
                        "link": "https://my.clevelandclinic.org/health/symptoms/21241-burping"
                    }
                }
            },
            "Gastritis": {
                "Stress Induced": {
                    "Nausea": {
                        "diagnosis": (
                            "Stress can trigger or worsen gastritis — inflammation of the stomach lining. "
                            "This may cause nausea, especially on an empty stomach or after meals. "
                            "Management includes stress reduction, bland foods, and possibly antacids."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/gastritis/symptoms-causes/syc-20355807"
                    },
                    "Stomach Tightness": {
                        "diagnosis": (
                            "A feeling of tightness or pressure in the upper abdomen is often linked to stress-related gastric inflammation. "
                            "This can be aggravated by anxiety, irregular eating, or excessive caffeine. "
                            "Relaxation practices and avoiding irritants may help."
                        ),
                        "link": "https://www.nhsinform.scot/illnesses-and-conditions/stomach-liver-and-gastrointestinal-tract/gastritis"
                    }
                },
                "Alcohol Intake": {
                    "Vomiting": {
                        "diagnosis": (
                            "Heavy or repeated alcohol consumption can erode the stomach lining, triggering nausea, inflammation, and vomiting. "
                            "This reaction is your body's way of expelling irritants. Avoiding alcohol and rehydrating are essential during recovery."
                        ),
                        "link": "https://www.hopkinsmedicine.org/health/conditions-and-diseases/alcoholic-gastritis"
                    },
                    "Bloating": {
                        "diagnosis": (
                            "Alcohol disrupts digestion and can lead to gas buildup and bloating. "
                            "It slows gastric emptying and can irritate the stomach. Limiting alcohol and consuming easily digestible foods may relieve symptoms."
                        ),
                        "link": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4291833/"
                    }
                }
            }
        },
        "Lower Abdominal": {
            "IBS": {
                "After Meals": {
                    "Cramping": {
                        "diagnosis": (
                            "Cramping after eating is a hallmark of irritable bowel syndrome (IBS), often due to hypersensitive gut nerves reacting to normal digestion. "
                            "This symptom may be triggered by certain foods or stress. Tracking food intake and managing stress levels can reduce flare-ups."
                        ),
                        "link": "https://www.niddk.nih.gov/health-information/digestive-diseases/irritable-bowel-syndrome"
                    },
                    "Urgency": {
                        "diagnosis": (
                            "Feeling a sudden, urgent need to use the bathroom after meals is a common IBS symptom. "
                            "It may be caused by accelerated bowel motility. Small, low-FODMAP meals and hydration may help control this response."
                        ),
                        "link": "https://www.aboutibs.org/symptoms/"
                    }
                },
                "Stress-related": {
                    "Flatulence": {
                        "diagnosis": (
                            "Excessive gas or bloating under stress is often related to how anxiety affects gut function. "
                            "This is particularly common in IBS patients. Reducing caffeine, carbonated drinks, and high-gas foods may help."
                        ),
                        "link": "https://www.medicalnewstoday.com/articles/321327"
                    },
                    "Constipation": {
                        "diagnosis": (
                            "Stress can disrupt normal digestion and slow bowel movements, leading to constipation. "
                            "This can worsen abdominal discomfort. Drinking more water, fiber, and adding light movement (e.g., walking) may ease symptoms."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/constipation/symptoms-causes/syc-20354253"
                    }
                }
            }
        }
    },


    "Insomnia": {
        "Trouble Falling Asleep": {
            "Racing Thoughts": {
                "Anxiety": {
                    "Heart Racing": {
                        "diagnosis": (
                            "A racing heart before bed is a common symptom of anxiety-related insomnia. "
                            "This physiological response is part of the fight-or-flight system, making it difficult for your body to enter a relaxed state. "
                            "Breathing exercises like 4-7-8 breathing or progressive muscle relaxation can help calm the nervous system before sleep."
                        ),
                        "link": "https://www.sleepfoundation.org/insomnia/anxiety-and-sleep"
                    },
                    "Overthinking": {
                        "diagnosis": (
                            "Overthinking at night often involves repetitive thoughts about the day or anticipation of tomorrow’s stressors. "
                            "This cognitive hyperarousal prevents mental wind-down. Techniques like brain dumping (writing everything on paper) and mindfulness can reduce cognitive load."
                        ),
                        "link": "https://www.healthline.com/health/mental-health/overthinking-at-night"
                    }
                },
                "Planning Tomorrow": {
                    "Mental Checklists": {
                        "diagnosis": (
                            "Rehearsing tasks or creating mental to-do lists before bed can delay sleep onset. "
                            "This type of future-oriented thinking is common in high-achievers or those under pressure. "
                            "Creating a written checklist earlier in the evening can prevent mental replay during sleep time."
                        ),
                        "link": "https://psychcentral.com/health/why-do-i-overthink-at-night"
                    },
                    "Calendar Worries": {
                        "diagnosis": (
                            "Stress about upcoming appointments, deadlines, or obligations can manifest as sleep disruption. "
                            "This anticipatory anxiety is often associated with perfectionism or fear of failure. "
                            "Breaking down plans into steps and scheduling prep earlier can reduce night-time worry."
                        ),
                        "link": "https://www.sleepfoundation.org/mental-health/stress-and-sleep"
                    }
                }
            },
            "Noise Disruption": {
                "Urban Environment": {
                    "Car Sounds": {
                        "diagnosis": (
                            "External noise such as traffic can fragment sleep or delay its onset. "
                            "Even if you habituate to noise, your brain may still register it subconsciously. "
                            "White noise machines or earplugs can mask disruptive sounds and improve sleep quality."
                        ),
                        "link": "https://www.sleepfoundation.org/noise-and-sleep"
                    },
                    "Sirens": {
                        "diagnosis": (
                            "Sudden, high-pitched urban sounds like sirens can trigger a startle response, making it hard to fall or stay asleep. "
                            "Light sleepers are particularly sensitive. Soundproofing curtains or noise-cancelling options may help."
                        ),
                        "link": "https://www.sleep.org/how-noise-affects-sleep/"
                    }
                },
                "Roommates": {
                    "Talking Late": {
                        "diagnosis": (
                            "Late-night conversations or disturbances from roommates can interrupt sleep hygiene. "
                            "Establishing quiet hours or using noise-blocking headphones can help preserve a calming nighttime routine."
                        ),
                        "link": "https://www.sleepfoundation.org/sleep-hygiene"
                    },
                    "Music": {
                        "diagnosis": (
                            "Music that is too upbeat, loud, or lyrically engaging can interfere with sleep onset. "
                            "While calming instrumental music may help, stimulating sounds may delay relaxation. "
                            "Choose slow, ambient tracks and avoid headphones while sleeping."
                        ),
                        "link": "https://www.sleepfoundation.org/noise-and-sleep/music"
                    }
                }
            }
        },
        "Waking Up Frequently": {
            "Nightmares": {
                "Past Trauma": {
                    "Flashbacks": {
                        "diagnosis": (
                            "Frequent nightmares involving flashbacks are a hallmark of trauma-related insomnia, often linked to PTSD. "
                            "These can trigger abrupt awakenings and difficulty returning to sleep. "
                            "Working with a trauma-informed therapist and using sleep-safe coping techniques is recommended."
                        ),
                        "link": "https://www.nimh.nih.gov/health/topics/post-traumatic-stress-disorder-ptsd"
                    },
                    "Crying at Night": {
                        "diagnosis": (
                            "Waking up crying can be an emotional response to vivid dreams or unresolved distress. "
                            "This is common in individuals with trauma or deep grief. "
                            "Bedtime journaling and grounding exercises can reduce emotional overflow at night."
                        ),
                        "link": "https://psychcentral.com/health/waking-up-crying"
                    }
                },
                "Stress": {
                    "Exams": {
                        "diagnosis": (
                            "Anticipation of exams can disrupt REM sleep and trigger nighttime waking. "
                            "This is often caused by a hyperactive stress response. "
                            "Establishing a pre-sleep wind-down routine with no screen time or last-minute cramming can improve sleep continuity."
                        ),
                        "link": "https://www.sleepfoundation.org/students-and-sleep"
                    },
                    "Job Interviews": {
                        "diagnosis": (
                            "Sleep disruptions before a job interview stem from performance anxiety and fear of evaluation. "
                            "Even subconscious worries can cause restlessness or nightmares. "
                            "Practicing confidence-building affirmations or mock interviews earlier in the day may help ease the mental load."
                        ),
                        "link": "https://www.apa.org/news/press/releases/stress/2014/job-search"
                    }
                }
            },
            "Sleep Apnea": {
                "Snoring": {
                    "Dry Mouth": {
                        "diagnosis": (
                            "Persistent snoring and waking with a dry mouth may be signs of obstructive sleep apnea (OSA), a condition where the airway partially closes during sleep. "
                            "This can cause poor sleep quality and morning fatigue. "
                            "Sleep studies and possible CPAP therapy are recommended for evaluation and treatment."
                        ),
                        "link": "https://www.sleepfoundation.org/sleep-apnea"
                    },
                    "Fatigue": {
                        "diagnosis": (
                            "If you're experiencing chronic fatigue despite sleeping 7–8 hours, it may be due to undiagnosed sleep apnea. "
                            "Shallow or interrupted breathing reduces restorative sleep. "
                            "Medical diagnosis through a sleep test is advised to confirm and manage the condition."
                        ),
                        "link": "https://www.cdc.gov/sleep/about_sleep/sleep_apnea.html"
                    }
                },
                "Interrupted Breathing": {
                    "Choking Sensation": {
                        "diagnosis": (
                            "Waking up gasping or choking is a red flag for moderate to severe sleep apnea. "
                            "This occurs when the airway closes entirely for brief periods, depriving the brain of oxygen. "
                            "Sleeping on your side and seeking professional evaluation is essential."
                        ),
                        "link": "https://www.nhlbi.nih.gov/health/sleep-apnea"
                    },
                    "Gasping": {
                        "diagnosis": (
                            "Gasping for air during sleep is an involuntary response to oxygen deprivation, common in obstructive sleep apnea. "
                            "This can increase cardiovascular risk if left untreated. A formal sleep study and treatment plan (e.g., CPAP) are important next steps."
                        ),
                        "link": "https://my.clevelandclinic.org/health/diseases/8709-obstructive-sleep-apnea"
                    }
                }
            }
        }
    },


    "Menstrual Problems": {
        "Cramps": {
            "Mild": {
                "Day 1 of Period": {
                    "Aching": {
                        "diagnosis": (
                            "Mild cramping on the first day of menstruation is common due to the uterus contracting to shed its lining. "
                            "These contractions are triggered by prostaglandins, which can cause discomfort. "
                            "Over-the-counter pain relief, heat therapy, and hydration usually alleviate symptoms effectively."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/menstrual-cramps/symptoms-causes/syc-20374938"
                    },
                    "Fatigue": {
                        "diagnosis": (
                            "Fatigue during the start of a period may result from hormonal fluctuations and a temporary drop in iron levels due to blood loss. "
                            "This can cause physical exhaustion and mental fog. Rest, iron-rich foods, and gentle movement can help restore energy levels."
                        ),
                        "link": "https://www.healthline.com/health/womens-health/menstrual-fatigue"
                    }
                },
                "Relieved by Heat": {
                    "Hot Water Bag": {
                        "diagnosis": (
                            "Applying a hot water bag to the lower abdomen helps relax the muscles of the uterus and improve blood flow, "
                            "which can reduce cramping. Heat works similarly to pain relievers by easing muscle tension and dulling discomfort."
                        ),
                        "link": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4455624/"
                    },
                    "Warm Bath": {
                        "diagnosis": (
                            "Soaking in a warm bath can alleviate mild menstrual cramps by promoting relaxation and reducing muscle tension. "
                            "Adding Epsom salts may provide additional relief due to their magnesium content, which helps with muscle relaxation."
                        ),
                        "link": "https://my.clevelandclinic.org/health/symptoms/21636-menstrual-cramps"
                    }
                }
            },
            "Severe": {
                "Vomiting": {
                    "Dehydration": {
                        "diagnosis": (
                            "Severe menstrual cramps can lead to nausea and vomiting, which in turn may cause dehydration if fluids are not replenished. "
                            "Staying hydrated with electrolyte solutions and resting in a dark, quiet environment may help manage symptoms. "
                            "Persistent vomiting should be discussed with a healthcare provider."
                        ),
                        "link": "https://www.medicalnewstoday.com/articles/severe-menstrual-cramps"
                    },
                    "Dizziness": {
                        "diagnosis": (
                            "Dizziness during menstruation may be linked to pain-related vasodilation, low blood pressure, or dehydration from vomiting. "
                            "It’s important to lie down, stay hydrated, and eat small, regular meals. If dizziness is severe or frequent, seek medical attention."
                        ),
                        "link": "https://www.healthline.com/health/menstrual-cramps-dizziness"
                    }
                },
                "Fainting": {
                    "Missed School/Work": {
                        "diagnosis": (
                            "Fainting or feeling faint due to severe menstrual pain can significantly impact daily functioning. "
                            "This may be a sign of dysmenorrhea or underlying conditions like endometriosis. "
                            "If pain causes frequent absences from school or work, a gynecological evaluation is recommended."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/endometriosis/symptoms-causes/syc-20354656"
                    },
                    "Emergency Visit": {
                        "diagnosis": (
                            "Severe menstrual pain accompanied by fainting, vomiting, or inability to function may warrant an emergency evaluation. "
                            "Such symptoms can signal complications like ovarian cysts or fibroids. If pain becomes unmanageable, seek immediate care."
                        ),
                        "link": "https://www.cdc.gov/reproductivehealth/infertility/index.htm"
                    }
                }
            }
        },
        "Irregular Periods": {
            "Missed Cycles": {
                "PCOS": {
                    "Acne": {
                        "diagnosis": (
                            "Persistent acne along with missed periods may indicate polycystic ovary syndrome (PCOS), a hormonal disorder that affects ovulation. "
                            "Elevated androgen levels can lead to acne, oily skin, and irregular cycles. Treatment often involves hormonal regulation and lifestyle changes."
                        ),
                        "link": "https://www.nichd.nih.gov/health/topics/pcos"
                    },
                    "Hair Growth": {
                        "diagnosis": (
                            "Unusual facial or body hair growth (hirsutism) in combination with irregular periods can be a sign of PCOS. "
                            "This occurs due to excess androgens. Medical treatment may include hormonal therapy or anti-androgen medications."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/pcos/symptoms-causes/syc-20353439"
                    }
                },
                "Stress": {
                    "Hormonal Disruption": {
                        "diagnosis": (
                            "Chronic stress affects the hypothalamic-pituitary-adrenal (HPA) axis, which can disrupt the menstrual cycle by altering hormone levels. "
                            "Missed or delayed periods are common in times of emotional or physical stress. Stress management and adequate rest often restore normalcy."
                        ),
                        "link": "https://www.healthline.com/health/stress/effects-on-body"
                    },
                    "Emotional Changes": {
                        "diagnosis": (
                            "Mood swings, irritability, or emotional sensitivity in tandem with irregular periods may be stress-induced. "
                            "Fluctuations in cortisol and estrogen can heighten emotional responses. Techniques like journaling, breathing, or therapy can help regulate emotions."
                        ),
                        "link": "https://psychcentral.com/stress/how-stress-affects-your-period"
                    }
                }
            }
        }
    },


    "Back Pain": {
        "Lower Back": {
            "Muscle Strain": {
                "Lifting Heavy Objects": {
                    "Sudden Twinge": {
                        "diagnosis": (
                            "A sharp or sudden twinge in the lower back during lifting likely indicates a muscle or ligament strain. "
                            "This can happen when lifting improperly or exceeding your body’s tolerance. Rest, ice, and anti-inflammatory medications typically aid recovery."
                        ),
                        "link": "https://www.spine-health.com/conditions/lower-back-pain/lower-back-strain"
                    },
                    "Soreness": {
                        "diagnosis": (
                            "Post-lifting soreness in the lower back is often due to overexertion or improper lifting posture. "
                            "While usually self-limiting, it’s important to avoid further strain. Gentle stretching and core strengthening exercises may aid healing."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/back-pain/symptoms-causes/syc-20369906"
                    }
                },
                "Poor Posture": {
                    "Long Sitting Hours": {
                        "diagnosis": (
                            "Extended sitting, especially with poor posture, can cause tension in the lumbar spine and hip flexors. "
                            "This strain may lead to chronic discomfort. Regular breaks, lumbar support, and posture correction can help alleviate symptoms."
                        ),
                        "link": "https://www.clevelandclinic.org/health/diseases/4488-posture-related-back-pain"
                    },
                    "Stiffness": {
                        "diagnosis": (
                            "Stiffness from prolonged sitting often stems from decreased mobility in spinal joints and tight surrounding muscles. "
                            "Incorporating hourly movement, stretching, and a standing desk can help reduce symptoms."
                        ),
                        "link": "https://www.spine-health.com/blog/7-tips-relieve-back-pain-your-desk-job"
                    }
                }
            }
        },
        "Upper Back": {
            "Posture-related": {
                "Desk Jobs": {
                    "Slouching": {
                        "diagnosis": (
                            "Poor ergonomics or slouching at a desk can lead to upper back and shoulder strain. "
                            "This posture misalignment causes muscle fatigue and joint stress. Maintaining an upright seated position and adjusting screen height may improve symptoms."
                        ),
                        "link": "https://my.clevelandclinic.org/health/articles/14302-ergonomics"
                    },
                    "Shoulder Pain": {
                        "diagnosis": (
                            "Upper back and shoulder pain during desk work often arises from tension in the trapezius muscles. "
                            "It may be worsened by forward head posture and lack of movement. Frequent breaks and shoulder rolls may offer relief."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/back-pain/symptoms-causes/syc-20369906"
                    }
                },
                "Mobile Overuse": {
                    "Tech Neck": {
                        "diagnosis": (
                            "Spending extended time on phones or laptops with a downward neck tilt can cause 'tech neck,' a repetitive strain injury. "
                            "This posture overloads the cervical spine. Holding devices at eye level and taking breaks reduces impact."
                        ),
                        "link": "https://www.spine-health.com/blog/6-tips-prevent-tech-neck"
                    },
                    "Fatigue": {
                        "diagnosis": (
                            "Neck and shoulder fatigue from device overuse is often due to muscle strain and poor support. "
                            "Symptoms may include tightness, soreness, or heaviness in the upper back. Supportive posture and screen breaks are helpful solutions."
                        ),
                        "link": "https://www.healthline.com/health/tech-neck"
                    }
                }
            }
        },
        "Neuropathic": {
            "Sciatica": {
                "Shooting Pain": {
                    "Down the Leg": {
                        "diagnosis": (
                            "Sciatica is characterized by shooting pain that radiates from the lower back through the buttock and down the leg. "
                            "It occurs when the sciatic nerve is compressed, often by a herniated disc or spinal narrowing. Physical therapy and anti-inflammatory treatments are common approaches."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/sciatica/symptoms-causes/syc-20377435"
                    },
                    "Numbness": {
                        "diagnosis": (
                            "Numbness in the leg, especially when paired with back pain, can indicate nerve impingement from conditions like sciatica. "
                            "This signals reduced sensory input due to pressure on the sciatic nerve. Medical evaluation is advised if symptoms persist or worsen."
                        ),
                        "link": "https://www.spine-health.com/conditions/sciatica/sciatica-symptoms"
                    }
                },
                "Prolonged Sitting": {
                    "Worsened Pain": {
                        "diagnosis": (
                            "Sciatic pain often intensifies after long periods of sitting, especially with poor posture. "
                            "This position increases pressure on spinal discs and nerves. Standing breaks and lumbar support can alleviate discomfort."
                        ),
                        "link": "https://www.healthline.com/health/back-pain/sitting-sciatica"
                    },
                    "Tingling": {
                        "diagnosis": (
                            "Tingling or 'pins and needles' sensations in the legs may result from sciatic nerve compression. "
                            "This symptom is known as paresthesia. Consistent symptoms should be evaluated to prevent nerve damage."
                        ),
                        "link": "https://www.medicalnewstoday.com/articles/tingling-in-left-leg"
                    }
                }
            }
        }
    },


    "Allergies": {
        "Food Allergies": {
            "Dairy": {
                "Milk": {
                    "Bloating": {
                        "diagnosis": (
                            "Bloating after consuming milk may indicate a lactose intolerance or dairy allergy. "
                            "In lactose intolerance, the body lacks the enzyme lactase to digest milk sugar, causing gas and bloating. "
                            "Switching to lactose-free alternatives or using lactase supplements may help."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/lactose-intolerance/symptoms-causes/syc-20374232"
                    },
                    "Diarrhea": {
                        "diagnosis": (
                            "Diarrhea following milk consumption can occur due to lactose intolerance or a food allergy. "
                            "In intolerance, undigested lactose draws water into the colon. Allergy symptoms may include additional immune responses. "
                            "A food allergy test can help distinguish between the two."
                        ),
                        "link": "https://www.niaid.nih.gov/diseases-conditions/food-allergy"
                    }
                },
                "Cheese": {
                    "Rash": {
                        "diagnosis": (
                            "A rash after eating cheese may be an allergic reaction to casein (milk protein) or food preservatives. "
                            "Such reactions are typically immune-mediated and may also include hives or swelling. Consult an allergist for testing and guidance."
                        ),
                        "link": "https://www.aafa.org/food-allergies/"
                    },
                    "Itchy Mouth": {
                        "diagnosis": (
                            "An itchy mouth after cheese may be a mild oral allergic reaction. "
                            "In some cases, it's due to cross-reactivity between pollen and food proteins (oral allergy syndrome). "
                            "This symptom typically resolves quickly but should be monitored if it worsens."
                        ),
                        "link": "https://www.aaaai.org/tools-for-the-public/conditions-library/allergies/oral-allergy-syndrome"
                    }
                }
            }
        },
        "Environmental": {
            "Dust Mites": {
                "Bedding": {
                    "Sneezing": {
                        "diagnosis": (
                            "Dust mites commonly accumulate in pillows, mattresses, and bedding, causing sneezing upon waking. "
                            "These microscopic allergens trigger nasal inflammation in sensitive individuals. "
                            "Frequent washing of bedding in hot water and using allergen-proof covers can reduce exposure."
                        ),
                        "link": "https://www.cdc.gov/asthma/dust_mites.htm"
                    },
                    "Coughing": {
                        "diagnosis": (
                            "Persistent coughing in the morning or at night may be triggered by dust mites in bedding. "
                            "This type of allergic asthma response can be managed with inhalers and environmental controls like HEPA filters."
                        ),
                        "link": "https://www.aafa.org/allergy-dust-mites/"
                    }
                },
                "Carpet": {
                    "Irritation": {
                        "diagnosis": (
                            "Carpets trap dust mites and other allergens, especially in humid environments. "
                            "This can cause eye, throat, or skin irritation. Vacuuming with a HEPA filter and using hard flooring in high-sensitivity areas may help."
                        ),
                        "link": "https://www.niehs.nih.gov/health/topics/conditions/asthma/allergens/index.cfm"
                    },
                    "Red Eyes": {
                        "diagnosis": (
                            "Red, itchy, or watery eyes in dusty rooms may be a symptom of allergic conjunctivitis caused by dust mites or dander. "
                            "Using air purifiers and antihistamine eye drops may relieve discomfort."
                        ),
                        "link": "https://www.aao.org/eye-health/diseases/allergic-conjunctivitis"
                    }
                }
            }
        },
        "Pet Allergies": {
            "Cats": {
                "Fur Exposure": {
                    "Asthma": {
                        "diagnosis": (
                            "Exposure to cat fur or dander may trigger asthma symptoms such as wheezing, shortness of breath, or coughing. "
                            "Cat allergens are lightweight and airborne, making them hard to avoid without strict environmental controls."
                        ),
                        "link": "https://www.cdc.gov/asthma/faqs.htm"
                    },
                    "Eye Swelling": {
                        "diagnosis": (
                            "Contact with cat fur can cause allergic reactions involving swelling, redness, or itchiness around the eyes. "
                            "This is an immune response to Fel d 1, a protein found in cat saliva and skin flakes. "
                            "Minimizing contact and using antihistamines may reduce symptoms."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/pet-allergy/symptoms-causes/syc-20352192"
                    }
                },
                "Scratches": {
                    "Rash": {
                        "diagnosis": (
                            "An itchy rash at the site of a cat scratch may be due to cat scratch disease (a bacterial infection) or a localized allergic response. "
                            "If the rash spreads or is accompanied by fever, seek medical attention. Wash wounds thoroughly after any scratch."
                        ),
                        "link": "https://www.cdc.gov/healthypets/diseases/cat-scratch.html"
                    },
                    "Redness": {
                        "diagnosis": (
                            "Redness after a scratch is a typical local response, but when paired with swelling, pain, or pus, it may suggest infection. "
                            "Topical antibiotics and wound care are usually sufficient, but worsening symptoms should be evaluated."
                        ),
                        "link": "https://www.healthline.com/health/cat-scratch-disease"
                    }
                }
            }
        }
    },


    "Sleep Issues": {
        "Nightmares": {
            "Trauma-related": {
                "PTSD": {
                    "Flashbacks": {
                        "diagnosis": (
                            "Nightmares that include vivid, intrusive memories or flashbacks are often associated with post-traumatic stress disorder (PTSD). "
                            "These experiences can disrupt sleep and cause distress upon waking. "
                            "Treatment may include trauma-focused cognitive behavioral therapy (CBT), EMDR, or prescribed sleep aids."
                        ),
                        "link": "https://www.nimh.nih.gov/health/topics/post-traumatic-stress-disorder-ptsd"
                    },
                    "Insomnia": {
                        "diagnosis": (
                            "Frequent nightmares due to PTSD can lead to chronic insomnia, as the fear of disturbing dreams may cause sleep avoidance. "
                            "Managing the underlying trauma with therapy and using relaxation techniques at night can help restore rest."
                        ),
                        "link": "https://www.sleepfoundation.org/ptsd-and-sleep"
                    }
                },
                "Abuse History": {
                    "Night Sweats": {
                        "diagnosis": (
                            "A history of trauma or abuse can result in autonomic nervous system dysregulation, leading to night sweats. "
                            "This is particularly common when sleep is interrupted by vivid or distressing dreams. "
                            "Stress management and trauma-informed therapy can help manage symptoms."
                        ),
                        "link": "https://www.sleepfoundation.org/sleep-disorders/night-sweats"
                    },
                    "Fear of Sleep": {
                        "diagnosis": (
                            "Avoidance of sleep due to fear of reliving traumatic events in dreams is common in those with past abuse. "
                            "This can worsen sleep deprivation and emotional regulation. "
                            "Safe sleep environments, grounding rituals, and therapy may help rebuild a sense of nighttime safety."
                        ),
                        "link": "https://psychcentral.com/ptsd/ptsd-and-nightmares"
                    }
                }
            }
        },
        "Restless Sleep": {
            "Caffeine": {
                "Late Night Coffee": {
                    "diagnosis": (
                            "Drinking coffee or other caffeine-containing beverages late in the evening can interfere with the body’s ability to fall asleep and enter deep sleep stages. "
                            "Caffeine blocks adenosine, a brain chemical that promotes sleepiness, leading to difficulty initiating rest. Avoid caffeine at least 6 hours before bedtime."
                        ),
                        "link": "https://www.sleepfoundation.org/nutrition/caffeine-and-sleep"
                    },
                "Jittery Feel": {
                    "diagnosis": (
                        "Feeling jittery or restless after caffeine is a sign of overstimulation. "
                        "This can result in a racing heart, fidgeting, and a general inability to relax, all of which impair sleep quality. "
                        "Reducing intake and switching to herbal alternatives like chamomile can support sleep."
                    ),
                    "link": "https://www.healthline.com/nutrition/caffeine-side-effects#nervousness-and-restlessness"
                }
            },
            "Energy Drinks": {
                "Light Sleep": {
                    "diagnosis": (
                        "Energy drinks contain high amounts of caffeine and sugar, which can lead to light, fragmented sleep even hours after consumption. "
                        "They also interfere with REM sleep cycles, leading to less restorative rest. "
                        "Avoiding stimulants after midday may improve sleep depth and duration."
                    ),
                    "link": "https://www.sleepfoundation.org/nutrition/energy-drinks-and-sleep"
                },
                "Wakefulness": {
                    "diagnosis": (
                        "If you feel alert and unable to wind down after consuming energy drinks, it’s likely due to their stimulating effect on the central nervous system. "
                        "These drinks can delay melatonin release and disrupt the body’s circadian rhythm. "
                        "Switching to decaffeinated drinks in the evening is recommended."
                    ),
                    "link": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6778826/"
                }
            }
        }
    },


    "Headaches": {
        "Tension Headaches": {
            "Stress": {
                "Workload": {
                    "Tight Forehead": {
                        "diagnosis": (
                            "Tension headaches due to heavy workload often cause a dull, tight pressure around the forehead or temples. "
                            "They result from prolonged stress, poor posture, and clenching of facial or neck muscles. "
                            "Stress management, stretching, and regular breaks can help relieve symptoms."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/tension-headache/symptoms-causes/syc-20353977"
                    },
                    "Eye Pain": {
                        "diagnosis": (
                            "Eye pain during stressful periods, especially when using screens, may result from tension headaches or eye strain. "
                            "This type of pain often radiates from the forehead or behind the eyes. "
                            "Frequent screen breaks, hydration, and posture adjustment can reduce discomfort."
                        ),
                        "link": "https://www.nhs.uk/conditions/tension-headaches/"
                    }
                },
                "Exams": {
                    "Temple Pressure": {
                        "diagnosis": (
                            "Exams and academic stress can trigger tension-type headaches, often described as pressure around the temples or a tight band around the head. "
                            "This can be managed with proper sleep, relaxation exercises, and hydration during study sessions."
                        ),
                        "link": "https://my.clevelandclinic.org/health/diseases/9631-tension-headaches"
                    },
                    "Nausea": {
                        "diagnosis": (
                            "While not typical for tension headaches, nausea can occur with prolonged stress and exhaustion. "
                            "If nausea frequently accompanies headaches, it may indicate a migraine pattern and should be evaluated by a doctor."
                        ),
                        "link": "https://www.webmd.com/migraines-headaches/guide/headache-symptoms"
                    }
                }
            }
        },
        "Migraines": {
            "Aura": {
                "Light Sensitivity": {
                    "Room Darkening": {
                        "diagnosis": (
                            "Sensitivity to light (photophobia) during a migraine with aura often leads to a strong desire to retreat to a dark room. "
                            "This symptom is part of the neurological cascade that precedes or accompanies migraine episodes. "
                            "Avoiding bright screens and resting in dim environments may help reduce intensity."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/migraine-with-aura/symptoms-causes/syc-20352072"
                    },
                    "Eye Pain": {
                        "diagnosis": (
                            "Migraines can cause pain behind or around one eye, sometimes mistaken for sinus issues. "
                            "This discomfort may increase with movement or light exposure. Migraine-specific medications and lifestyle changes are commonly used treatments."
                        ),
                        "link": "https://www.medicalnewstoday.com/articles/migraine-behind-the-eye"
                    }
                },
                "Nausea": {
                    "Vomiting": {
                        "diagnosis": (
                            "Nausea and vomiting are common migraine symptoms, especially when triggered by sensory overload. "
                            "These occur due to the effect of migraines on brainstem regions that control digestion. Rest, hydration, and anti-nausea medication may help manage these episodes."
                        ),
                        "link": "https://www.healthline.com/health/migraine/migraine-and-nausea"
                    },
                    "Dizziness": {
                        "diagnosis": (
                            "Migraine-related dizziness may present as vertigo or a general sense of imbalance. "
                            "This occurs due to disruption in the brain's vestibular system. Vestibular therapy and migraine medication can be useful treatments."
                        ),
                        "link": "https://www.americanmigrainefoundation.org/resource-library/vestibular-migraine/"
                    }
                }
            }
        },
        "Cluster Headaches": {
            "Behind Eyes": {
                "Stabbing Sensation": {
                    "Tearing": {
                        "diagnosis": (
                            "Cluster headaches are excruciating, sharp pains typically behind one eye, often accompanied by tearing. "
                            "These headaches occur in cyclical patterns or 'clusters' and are usually unilateral. Treatment may include oxygen therapy and preventive medications."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/cluster-headache/symptoms-causes/syc-20352080"
                    },
                    "Swelling": {
                        "diagnosis": (
                            "Swelling around one eye during a cluster headache is a common autonomic symptom. "
                            "It can be accompanied by nasal congestion or a drooping eyelid on the affected side. Immediate treatment is important to relieve pain."
                        ),
                        "link": "https://www.ninds.nih.gov/health-information/disorders/cluster-headaches"
                    }
                },
                "Short Duration": {
                    "30-45 Minutes": {
                        "diagnosis": (
                            "Cluster headaches are brief but intense, typically lasting 30 to 90 minutes. "
                            "They often strike at the same time daily for weeks and can be misdiagnosed as sinus headaches. "
                            "Accurate diagnosis is crucial to initiate targeted therapy."
                        ),
                        "link": "https://www.nhs.uk/conditions/cluster-headaches/"
                    },
                    "Sharp Onset": {
                        "diagnosis": (
                            "Cluster headaches begin abruptly and reach peak intensity within minutes. "
                            "This sudden onset differentiates them from migraines. Immediate use of prescribed fast-acting treatments is advised once an attack begins."
                        ),
                        "link": "https://www.verywellhealth.com/cluster-headaches-overview-4171544"
                    }
                }
            }
        }
    },


    "Joint Pain": {
        "Arthritis": {
            "Rheumatoid": {
                "Morning Stiffness": {
                    "Lasts > 1 hr": {
                        "diagnosis": (
                            "Stiffness in the joints lasting more than an hour after waking is a classic sign of rheumatoid arthritis (RA). "
                            "RA is an autoimmune disorder where the immune system attacks the joints, causing inflammation. "
                            "Treatment includes disease-modifying antirheumatic drugs (DMARDs), physical therapy, and anti-inflammatories."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/rheumatoid-arthritis/symptoms-causes/syc-20353648"
                    },
                    "Fatigue": {
                        "diagnosis": (
                            "Fatigue in RA is caused by systemic inflammation and the body’s immune response. "
                            "It can be persistent even when joint symptoms are controlled. Rest, light activity, and managing inflammation through medication can help."
                        ),
                        "link": "https://www.arthritis.org/diseases/rheumatoid-arthritis"
                    }
                },
                "Joint Inflammation": {
                    "Swelling": {
                        "diagnosis": (
                            "RA frequently causes visible joint swelling due to ongoing inflammation. "
                            "This may be warm to the touch and can reduce mobility. Early diagnosis is key to preventing long-term joint damage."
                        ),
                        "link": "https://www.rheumatology.org/I-Am-A/Patient-Caregiver/Diseases-Conditions/Rheumatoid-Arthritis"
                    },
                    "Redness": {
                        "diagnosis": (
                            "Redness around a joint typically reflects active inflammation. "
                            "In RA, this is part of the autoimmune attack on the synovial lining. Anti-inflammatory medications and immunosuppressants may be used to reduce symptoms."
                        ),
                        "link": "https://www.nhs.uk/conditions/rheumatoid-arthritis/"
                    }
                }
            },
            "Osteoarthritis": {
                "Wear and Tear": {
                    "Pain with Movement": {
                        "diagnosis": (
                            "Osteoarthritis (OA) is caused by cartilage breakdown, leading to joint pain during movement. "
                            "Pain often worsens with activity and improves with rest. Management includes weight control, joint-friendly exercise, and NSAIDs."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/osteoarthritis/symptoms-causes/syc-20351925"
                    },
                    "Bone Spurs": {
                        "diagnosis": (
                            "Bone spurs, or osteophytes, are bony projections that form in joints with OA. "
                            "They can cause stiffness and restrict range of motion. Physical therapy and, in severe cases, surgery may be required."
                        ),
                        "link": "https://www.cedars-sinai.org/health-library/diseases-and-conditions/b/bone-spur.html"
                    }
                },
                "Aging": {
                    "Knee Pain": {
                        "diagnosis": (
                            "Knee pain with age is frequently due to osteoarthritis, where years of use wear down the cartilage cushioning the joint. "
                            "Pain may occur during walking or climbing stairs. Treatment includes supportive footwear, joint-friendly exercises, and weight loss if needed."
                        ),
                        "link": "https://orthoinfo.aaos.org/en/diseases--conditions/knee-osteoarthritis/"
                    },
                    "Finger Deformity": {
                        "diagnosis": (
                            "In OA, fingers may develop deformities such as Heberden’s or Bouchard’s nodes — bony enlargements of the joints. "
                            "These changes may be painless or associated with stiffness and reduced dexterity. Splints and hand therapy can support function."
                        ),
                        "link": "https://www.arthritis.org/diseases/osteoarthritis"
                    }
                }
            }
        },
        "Injury": {
            "Sports Injury": {
                "Ligament Tear": {
                    "Swelling": {
                        "diagnosis": (
                            "Swelling after a sports-related ligament tear (such as ACL or ankle sprain) is caused by internal bleeding and inflammation. "
                            "Immediate treatment includes R.I.C.E. (Rest, Ice, Compression, Elevation) and orthopedic evaluation."
                        ),
                        "link": "https://www.mayoclinic.org/diseases-conditions/knee-ligament-injury/symptoms-causes/syc-20350879"
                    },
                    "Inability to Move": {
                        "diagnosis": (
                            "If joint movement is significantly restricted after a ligament tear, it may indicate structural instability or severe injury. "
                            "Do not force motion — seek medical imaging and possible surgical consultation."
                        ),
                        "link": "https://www.ncbi.nlm.nih.gov/books/NBK499903/"
                    }
                },
                "Sprain": {
                    "Local Pain": {
                        "diagnosis": (
                            "Localized joint pain after twisting or overextending may be due to a mild-to-moderate sprain. "
                            "Pain typically centers around the affected ligament. Rest and temporary immobilization can help recovery."
                        ),
                        "link": "https://www.cdc.gov/ncbddd/jointhealth/jointinjuries.html"
                    },
                    "Bruising": {
                        "diagnosis": (
                            "Bruising after a sprain indicates minor internal bleeding in the soft tissues surrounding the joint. "
                            "This is common in ankle and wrist injuries. Elevation and ice can minimize discoloration and swelling."
                        ),
                        "link": "https://www.hopkinsmedicine.org/health/conditions-and-diseases/sprains-and-strains"
                    }
                }
            }
        }
    },

}
