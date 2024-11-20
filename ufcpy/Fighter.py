from typing import Optional
from bs4 import BeautifulSoup 

from .core import parse, find_element

def find_fighter_by_fullname(fighter: str):
    base_url = "https://ufc.com/athlete"
    url = fighter.lower().replace(" ", "-")
    parsed_url = parse(f"{base_url}/{url}")
    return Fighter(parsed_url)

class Fighter:
    def __init__(self, _parsed_url: BeautifulSoup):
        self._parsed_url = _parsed_url
        self._bio = find_element(_parsed_url, "div", clas="c-bio__info-details")

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        """:class:`str`: The full name of the fighter"""
        return (
            find_element(self._parsed_url, "h1", clas="hero-profile__name")
            .get_text()
            .strip()
        )

    @property
    def nickname(self) -> Optional[str]:
        """:class:`str`: The nickname of the fighter"""
        try:
            return (
                find_element(self._parsed_url, "p", clas="hero-profile__nickname")
                .get_text()
                .strip('/"')
            )
        except:
            return None
        
    @property
    def age(self) -> int:
        """:class:`int`: The age of the fighter"""
        return int(
            self._bio.find("div", string="Age")
            .find_next_sibling()
            .get_text()
            .strip()
        )
    
    @property
    def division(self) -> str:
        """:class:`str`: The division the fighter is currently particapting in"""
        return (
            find_element(self._parsed_url, "p", clas="hero-profile__division-title")
            .get_text()
            .strip()
        )

    @property
    def gender(self) -> str:
        """:class:`str`: The gender of the fighter"""
        if "Women's" in self.division:
            return "Woman"
        else:
            return "Man"

    @property
    def record(self) -> str:
        """:class:`str`: The record of the fighter in the format of WIN-LOSS-DRAW"""
        return (
            find_element(self._parsed_url, "p", clas="hero-profile__division-body")
            .get_text()
            .split()[0]
            .strip()
        )

    @property
    def wins(self) -> int:
        """:class:`int`: Amount of wins the fighter have"""
        return int(
            self.record
            .split("-")[0]
            .strip()
        )

    @property
    def losses(self) -> int:
        """:class:`int`: Amount of losses the fighter have"""
        return int(
            self.record
            .split("-")[1]
            .strip()
        )

    @property
    def draws(self) -> int:
        """:class:`int`: Amount of draws the fighter have"""
        return int(
            self.record
            .split("-")[2]
            .strip()
        )

    @property
    def weight(self) -> float:
        """:class:`float`: The weight the fighter likes to compete at"""
        return float(
            self._bio.find("div", string="Weight")
            .find_next_sibling()
            .get_text()
            .strip()
        )

    @property
    def hometown(self) -> str:
        """:class:`str`: The hometown of the fighter"""
        return (
            self._bio.find("div", string="Hometown")
            .find_next_sibling()
            .get_text()
            .strip()
        )

    @property
    def activity(self) -> str:
        """:class:`str`: The activity of the fighter"""
        return (
            self._bio.find("div", string="Status")
            .find_next_sibling()
            .get_text()
            .strip()
        )

    @property
    def image_url(self) -> str:
        """:class:`str`: A image of the fighter"""
        return (
            find_element(self._parsed_url, "img", clas="hero-profile__image")
            .get("src") 
        )

    @property
    def height_in_inch(self) -> Optional[float]:
        """Optional[:class:`float`]: The fighter's height in inches"""
        try:
            return float(
                self._bio.find("div", string="Height")
                .find_next_sibling()
                .get_text()
                .strip()
            )
        except:
            return None
    
    @property
    def height_in_feet(self) -> Optional[str]:
        """Optional[:class:`str`]: The fighter's height in feet"""
        try:
            height_feet = round(self.height_in_inch / 12, 1)
            new_height = str(height_feet).replace(".", " ").split(" ")
            if new_height[1] == "0":
                return f"{new_height[0]} foot"
            else:
                return f"{new_height[0]} foot {new_height[1]} inch"
        except:
            return None

    @property
    def reach(self) -> Optional[str]:
        """Optional[:class:`str`]: The reach of the fighter"""
        try:
            return float(
                self._bio.find("div", string="Reach")
                .find_next_sibling()
                .get_text()
                .strip()
            )
        except:
            return None

    @property
    def leg_reach(self) -> Optional[str]:
        """Optional[:class]:`str`: The leg reach of the fighter"""
        try:
            return float(
                self._bio.find("div", string="Leg reach")
                .find_next_sibling()
                .get_text()
            )
        except:
            return None
        
    @property
    def octagon_debut(self) -> Optional[str]:
        """Optional[:class: `str`]: The date of when the fighter first fought in the UFC octagon"""
        try:
            return (
                self._bio.find("div", string="Octagon Debut")
                .find_next_sibling()
                .get_text()
                .strip()
            )
        except:
            return None

    @property
    def trains_at(self) -> Optional[str]:
        """Optional[:class: `str`]: The gym the UFC fighter currently trains out of"""
        try:
            return (
                self._bio.find("div", string="Trains at")
                .find_next_sibling()
                .get_text()
                .strip()
            )
        except:
            return None

    @property
    def striking_accuracy(self) -> int:
        """:class:`int`: The striking accuracy percentage in the UFC career of the fighter"""
        return int(
            find_element(self._parsed_url, "text", clas="e-chart-circle__percent", find_all=True)
            [0].get_text()
            .strip("%")
        )

    @property
    def significant_strikes_landed(self) -> int:
        """:class:`int`: The significant strikes landed in the UFC career of the fighter"""
        return int(
            find_element(self._parsed_url, "dl", clas="c-overlap__stats")
            .find_next("dd")
            .get_text()
            .strip()
        )

    @property
    def significant_strikes_attempted(self) -> int:
        """:class:`int`: The significant strikes attemped in the UFC career of the fighter"""
        return int(
            find_element(self._parsed_url, "dl", clas="c-overlap__stats")
            .find_next_sibling()
            .find_next("dd")
            .get_text()
            .strip()
        )

    @property
    def takedown_accuracy(self) -> int:
        """:class:`int`: The takedown accuracy percentage in the UFC career of the fighter"""
        return int(
            find_element(self._parsed_url, "text", clas="e-chart-circle__percent", find_all=True)
            [1].get_text()
            .strip("%")    
        )

    @property
    def landed_takedowns(self) -> Optional[int]:
        """Optional[:class:`int`]: The takedowns landed in the UFC career of the fighter"""
        try:
            return int(
                find_element(self._parsed_url, "dl", clas="c-overlap__stats", find_all=True)
                [2].find_next("dd")
                .get_text()
                .strip()
            )
        except:
            return None

    @property
    def attempted_takedowns(self) -> Optional[int]:
        """Optional[:class:`str`]: The takedowns attempted in the UFC career of the fighter"""
        try:
            return int(
                find_element(self._parsed_url, "dl", clas="c-overlap__stats", find_all=True)
                [3].find_next("dd")
                .get_text()
                .strip()
            )
        except:
            return None
        
    @property
    def wins_by_ko(self) -> int:
        """:class:`int`: The amount of the knockout wins the fighter has in the UFC"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [3].get_text()
            .split(" ")[0]
        )
    
    @property
    def wins_by_ko_percentage(self) -> int:
        """:class:`int`: The percentage of the knockout wins the fighter has in the UFC"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [3].get_text()
            .split(" ")[1]
            .strip("(%)")
        )
        
    @property
    def wins_by_sub(self) -> int:
        """:class:`int`: The amount of the submission wins the fighter has in the UFC"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [5].get_text()
            .split(" ")[0]
        )
    
    @property
    def wins_by_sub_percentage(self) -> int:
        """:class:`int`: The percentage of the submission wins the fighter has in the UFC"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [5].get_text()
            .split(" ")[1]
            .strip("(%)")
        )
        
    @property
    def wins_by_dec(self) -> int:
        """:class:`int`: The amount of the decision wins the fighter has in the UFC"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [4].get_text()
            .split(" ")[0]
        )
    
    @property
    def wins_by_dec_percentage(self) -> int:
        """:class:`int`: The percentage of the decision wins the fighter has in the UFC"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [4].get_text()
            .split(" ")[1]
            .strip("(%)")
        )
        
    @property
    def sig_str_landed_min(self) -> float:
        """:class:`float`: The amount of signfication strikes the figher lands per minute"""
        return float(
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [0].get_text()
            .strip()
        )
    
    @property
    def sig_str_absorbed_min(self) -> float:
        """:class:`float`: The amount of signfication strikes the figher absorbs per minute"""
        return float(
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [1].get_text()
            .strip()
        )

    @property
    def takedown_avg(self) -> float:
        """:class:`float`: The average amount of takedowns the figher lands per fight"""
        return float(
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [2].get_text()
            .strip()
        )

    @property
    def submission_avg(self) -> float:
        """:class:`float`: The average amount of submissions the figher lands per fight"""
        return float(
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [3].get_text()
            .strip()
        )

    @property
    def sig_str_defense(self) -> int:
        """:class:`int`: The percentage of signfication strikes the figher defends against in whole UFC career"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [4].get_text()
            .strip()
        )

    @property
    def takedown_defense(self) -> int:
        """:class:`int`: The percentage of takedowns the figher defends against in whole UFC career"""
        return float(
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [5].get_text()
            .strip()
        )

    @property
    def knockdown_avg(self) -> float:
        """:class:`float`: The amount of knockdowns the figher lands per a 15 minute window"""
        return float(
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [6].get_text()
            .strip()
        )
    
    @property
    def average_fight_time(self) -> str:
        """:class:`str`: The average amount of time the fighter spends in octagon per fight"""
        return (
            find_element(self._parsed_url, "div", clas="c-stat-compare__number", find_all=True)
            [7].get_text()
            .strip()
        )
    
    @property
    def sig_str_via_standing(self) -> int:
        """:class:`int`: The amount of significant strikes the fighter has thrown in a standing position"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [0].get_text()
            .split(" ")[0]
        )
    
    @property
    def sig_str_percentage_via_standing(self) -> int:
        """:class:`int`: The percentage of significant strikes the fighter has thrown in a standing position"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [0].get_text()
            .split(" ")[1]
            .strip("(%)")
        )
    
    @property
    def sig_str_via_clinch(self) -> int:
        """:class:`int`: The amount of significant strikes the fighter has thrown in a clinch position"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [1].get_text()
            .split(" ")[0]
        )
    
    @property
    def sig_str_percentage_via_clinch(self) -> int:
        """:class:`int`: The percentage of significant strikes the fighter has thrown in a clinch position"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [1].get_text()
            .split(" ")[1]
            .strip("(%)")
        )

    @property
    def sig_str_via_ground(self) -> int:
        """:class:`int`: The amount of significant strikes the fighter has thrown in a ground position"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [2].get_text()
            .split(" ")[0]
        )
    
    @property
    def sig_str_percentage_via_ground(self) -> int:
        """:class:`int`: The percentage of significant strikes the fighter has thrown in a ground position"""
        return int(
            find_element(self._parsed_url, "div", clas="c-stat-3bar__value", find_all=True)
            [2].get_text()
            .split(" ")[1]
            .strip("(%)")
        )
    
    @property
    def sig_str_to_head(self) -> int:
        """:class:`int`: The amount of significant strikes the fighter has thrown to the head"""
        return int(
            find_element(self._parsed_url, "text", id="e-stat-body_x5F__x5F_head_value")
            .get_text()
            .strip()
        )
    
    @property
    def sig_str_percentage_to_head(self) -> int:
        """:class:`int`: The percentage of significant strikes the fighter has thrown to the head"""
        return int(
            find_element(self._parsed_url, "text", id="e-stat-body_x5F__x5F_head_percent")
            .get_text()
            .strip("%")
        )
    
    @property
    def sig_str_to_body(self) -> int:
        """:class:`int`: The amount of significant strikes the fighter has thrown to the body"""
        return int(
            find_element(self._parsed_url, "text", id="e-stat-body_x5F__x5F_body_value")
            .get_text()
            .strip()
        )
    
    @property
    def sig_str_percentage_to_body(self) -> int:
        """:class:`int`: The percentage of significant strikes the fighter has thrown to the body"""
        return int(
            find_element(self._parsed_url, "text", id="e-stat-body_x5F__x5F_body_percent")
            .get_text()
            .strip("%")
        )
    
    @property
    def sig_str_to_leg(self) -> int:
        """:class:`int`: The amount of significant strikes the fighter has thrown to the leg"""
        return int(
            find_element(self._parsed_url, "text", id="e-stat-body_x5F__x5F_leg_value")
            .get_text()
            .strip()
        )
    
    @property
    def sig_str_percentage_to_leg(self) -> int:
        """:class:`int`: The percentage of significant strikes the fighter has thrown to the leg"""
        return int(
            find_element(self._parsed_url, "text", id="e-stat-body_x5F__x5F_leg_percent")
            .get_text()
            .strip("%")
        )