import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft = 0, floors = 0) {
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
