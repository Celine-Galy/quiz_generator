from moviepy import concatenate_videoclips


def assembler_scenes(scenes):
    if not scenes:
        raise ValueError("Aucune scène vidéo n'a été créée.")

    return concatenate_videoclips(
        scenes,
        method="compose"
    )
