from Drawable import Drawable


class TerrainBlock(Drawable):

    def __init__(self, x=0, y=0, other=None):
        Drawable.__init__(self, x, y, other)

    def set_block_type(self, type):
        self.type = type
        # setTexture( & DJM::TextureManager::GetInstance()->GetTexture(mType));

    """DJM::Block & operator = (const
    DJM::Block & other){

        mType = other.GetBlockType();
    setSize(other.getSize());
    setPosition(other.getPosition());

    return *this;
    }"""